"""
04_tables_figures.py
Produce tables (output/tables/) and figures (output/figures/).
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

CLEAN = Path("data/clean")
TABLES = Path("output/tables")
FIGURES = Path("output/figures")
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)


def make_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Return a summary statistics table."""
    return df.describe().T[["count", "mean", "std", "min", "max"]]


if __name__ == "__main__":
    # df = pd.read_csv(CLEAN / "main_dataset_clean.csv")
    # summary = make_summary_statistics(df)
    # summary.to_latex(TABLES / "table1_summary_stats.tex", float_format="%.3f")
    pass
