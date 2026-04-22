"""
02_clean_data.py
Clean and transform data from data/clean/.
"""
import pandas as pd
from pathlib import Path

CLEAN = Path("data/clean")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning steps. Replace with your actual logic."""
    # Example steps:
    # df = df.dropna(subset=["your_key_variable"])
    # df = df[df["year"] >= 2000]
    raise NotImplementedError("Replace this with your actual cleaning code.")


if __name__ == "__main__":
    # df = pd.read_csv(CLEAN / "main_dataset.csv")
    # df_clean = clean_dataset(df)
    # df_clean.to_csv(CLEAN / "main_dataset_clean.csv", index=False)
    pass
