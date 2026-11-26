#!/usr/bin/env python3
# Save as make_funnel_graph.py
import json
import glob
import matplotlib.pyplot as plt

def main():
    files = glob.glob("scan_progress_seed*.jsonl")
    raw_count = 0
    extract_count = 0
    filter_count = 0

    for f in files:
        with open(f, "r") as file:
            for line in file:
                if not line.strip(): continue
                data = json.loads(line)
                raw_count += len(data.get("findings", []))
                
    # Count extracted
    for f in glob.glob("credentials_seed*.jsonl") + glob.glob("credentials_extracted*.jsonl"):
        with open(f, "r") as file:
            extract_count += sum(1 for line in file if line.strip())

    # Count filtered
    for f in glob.glob("worth_investigating*.jsonl"):
        with open(f, "r") as file:
            filter_count += sum(1 for line in file if line.strip())

    stages = ['Raw TruffleHog\nFindings', 'Extracted\nCredentials', 'High-Signal\n(Worth Investigating)']
    counts = [raw_count, extract_count, filter_count]
    colors = ['#d9534f', '#f0ad4e', '#5cb85c']

    plt.figure(figsize=(8, 5))
    bars = plt.barh(stages, counts, color=colors)
    
    plt.xlabel('Number of Records', fontsize=12)
    plt.title('Pipeline Noise Reduction Funnel', fontsize=14, fontweight='bold')
    
    # Add numbers to the end of the bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + (max(counts)*0.02), bar.get_y() + bar.get_height()/2, 
                 f'{int(width):,}', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig("graph_funnel.png", dpi=300)
    print("✅ Saved graph_funnel.png")

if __name__ == "__main__":
    main()
