"""Simple data loading utilities for Lab01.

The notebook is the main file for this lab. These helper functions are kept small
so the project structure is clean without becoming too advanced.
"""

from pathlib import Path
import pandas as pd


def find_csv_files(search_dirs, recursive=True):
    """Find CSV files in common upload folders.

    The function skips generated output folders so that rerunning the notebook
    does not accidentally reload processed files as raw data.
    """
    csv_files = []
    seen = set()
    skip_parts = {"outputs", "processed_data", ".ipynb_checkpoints", "__pycache__"}

    for folder in search_dirs:
        folder = Path(folder)
        if not folder.exists():
            continue

        patterns = ["*.csv"]
        if recursive:
            patterns.append("**/*.csv")

        for pattern in patterns:
            for file_path in folder.glob(pattern):
                if not file_path.is_file():
                    continue
                if any(part in skip_parts for part in file_path.parts):
                    continue
                if file_path.name.startswith("processed_"):
                    continue

                resolved = file_path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    csv_files.append(resolved)

    return sorted(csv_files)


def load_csv_files(csv_files):
    """Load all CSV files into a dictionary of pandas DataFrames."""
    datasets = {}

    for file_path in csv_files:
        file_path = Path(file_path)
        key = file_path.stem
        original_key = key
        counter = 1

        while key in datasets:
            counter += 1
            key = f"{original_key}_{counter}"

        datasets[key] = pd.read_csv(file_path)

    return datasets


def download_with_kagglehub(dataset_name="vanpatangan/readmission-dataset"):
    """Download the Kaggle dataset using KaggleHub as a backup option."""
    import kagglehub

    path = kagglehub.dataset_download(dataset_name)
    print("Path to dataset files:", path)
    return Path(path)
