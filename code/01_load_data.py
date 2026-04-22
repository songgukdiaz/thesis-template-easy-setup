"""
01_load_data.py
Load raw data from data/raw/ and save to data/clean/.
"""
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
CLEAN = Path("data/clean")
CLEAN.mkdir(parents=True, exist_ok=True)


def load_main_dataset():
    """Load the main dataset. Replace with your actual file and format."""
    # Example: df = pd.read_csv(RAW / "your_file.csv")
    raise NotImplementedError("Replace this with your actual data loading code.")


if __name__ == "__main__":
    df = load_main_dataset()
    print(f"Loaded {len(df):,} rows, {len(df.columns)} columns.")
    # Save cleaned version:
    # df.to_csv(CLEAN / "main_dataset.csv", index=False)
