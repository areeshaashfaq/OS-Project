#!/usr/bin/env python3
import json
import glob
import os
import matplotlib.pyplot as plt

def main():
    progress_files = glob.glob("scan_progress_seed*.jsonl")
    if not progress_files:
        print("No scan progress files found.")
        return

    # Data to plot
    seeds = []
    total_repos = []
    repos_with_findings = []

    for file_path in sorted(progress_files):
        # Extract the seed number from the filename (e.g., "scan_progress_seed6.jsonl" -> "6")
        seed_name = file_path.replace("scan_progress_seed", "").replace(".jsonl", "")
        
        total = 0
        with_findings = 0
        
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    total += 1
                    # Check if the 'findings' array is not empty
                    if data.get("findings") and len(data["findings"]) > 0:
                        with_findings += 1
                except json.JSONDecodeError:
                    pass

        if total > 0:
            seeds.append(f"Seed {seed_name}")
            total_repos.append(total)
            repos_with_findings.append(with_findings)

    if not seeds:
        print("No valid data found in progress files.")
        return

    # --- Plotting the Graph ---
    plt.figure(figsize=(10, 6))
    
    # Define X axis positions
    x = range(len(seeds))
    width = 0.35

    # Plot bars
    plt.bar([i - width/2 for i in x], total_repos, width, label='Repos Scanned', color='#4C72B0')
    plt.bar([i + width/2 for i in x], repos_with_findings, width, label='Repos with Findings', color='#C44E52')

    # Add labels and title
    plt.xlabel('Scan Batches (Seeds)', fontsize=12)
    plt.ylabel('Number of Repositories', fontsize=12)
    plt.title('Secret Detection Yield Rate Across Scanned Batches', fontsize=14, fontweight='bold')
    plt.xticks(x, seeds, fontsize=11)
    plt.legend(fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save and show
    plt.tight_layout()
    out_file = "scan_yield_graph.png"
    plt.savefig(out_file, dpi=300)
    print(f"✅ Successfully generated graph: {out_file}")
    
    # plt.show() # Uncomment this if you have a GUI setup and want it to pop up

if __name__ == "__main__":
    main()
