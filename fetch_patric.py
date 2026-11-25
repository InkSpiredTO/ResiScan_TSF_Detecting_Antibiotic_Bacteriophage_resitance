import pandas as pd
import subprocess
import os

# 1. Load the AMR table
df = pd.read_csv("data/PATRIC_genomes_AMR.txt", sep="\t", dtype=str)

# 2. Filter for entries with a valid MIC value (customize antibiotic or count as needed)
filtered = df.dropna(subset=["measurement_value"])
genome_ids = filtered["genome_id"].unique()[:50]  # Start with 20 genomes to test storage

print(f"Downloading {len(genome_ids)} genomes...")

# 3. Download .fna sequences directly into the Codespace via FTPS
for gid in genome_ids:
    url = f"ftp://ftp.bvbrc.org/genomes/{gid}/{gid}.fna"
    out_path = f"data/genomes/{gid}.fna"
    if not os.path.exists(out_path):
        subprocess.run(["curl", "--ftp-ssl", "-s", "-k", url, "-o", out_path])

print("Done! Files saved in data/genomes/")

