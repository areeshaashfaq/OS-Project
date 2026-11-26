import asyncio
import pandas as pd
from data_loader import load_credentials
from engine import GmailVerificationEngine
import os

async def main():
    # 1. Load Data
    credentials = load_credentials(source_type="mock", file_path="findings.json")
    
    if not credentials:
        print("No credentials loaded. Exiting.")
        return

    print(f"Loaded {len(credentials)} credentials.")
    
    # 2. Initialize Engine
    engine = GmailVerificationEngine(headless=True) # <--- Fixed
    await engine.start()
    
    # 3. Run Verification
    results = await engine.run_batch(credentials, concurrency=3)
    
    # 4. Save Results
    os.makedirs("output", exist_ok=True)
    df = pd.DataFrame(results)
    output_file = "output/verification_results.csv"
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    # 5. Cleanup
    await engine.stop()

if __name__ == "__main__":
    asyncio.run(main())