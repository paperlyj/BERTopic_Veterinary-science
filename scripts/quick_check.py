"""Quick dataset check for the veterinary science BERTopic repository."""
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_DIR / "data" / "raw" / "export_veterinary_science_scopus_2010_2025.csv.gz"

if not RAW_FILE.exists():
    raise FileNotFoundError(f"Raw dataset not found: {RAW_FILE}")

df = pd.read_csv(RAW_FILE, encoding="utf-8-sig", compression="infer", low_memory=False)
print("Raw Scopus export")
print("-----------------")
print(f"Rows:    {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")
print("
First columns:")
print(df.columns[:10].tolist())

if "Source title" in df.columns:
    print("
Top source titles:")
    print(df["Source title"].value_counts().head(20).to_string())
