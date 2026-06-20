"""Basic preprocessing utilities for Lab01."""

import re
import pandas as pd


TARGET_KEYWORDS = ["readmitted", "readmission", "readmit", "target", "outcome"]


def clean_column_names(df):
    """Clean column names using simple readable rules."""
    new_columns = []

    for col in df.columns:
        cleaned = str(col).strip().lower()
        cleaned = re.sub(r"\s+", "_", cleaned)
        cleaned = re.sub(r"[^a-z0-9_]+", "", cleaned)
        cleaned = re.sub(r"_+", "_", cleaned).strip("_")
        new_columns.append(cleaned)

    df = df.copy()
    df.columns = new_columns
    return df


def detect_target_column(df, keywords=None):
    """Detect the most likely readmission target column."""
    if keywords is None:
        keywords = TARGET_KEYWORDS

    columns = list(df.columns)

    for keyword in keywords:
        for col in columns:
            if keyword == col.lower():
                return col

    for keyword in keywords:
        for col in columns:
            if keyword in col.lower():
                return col

    return None


def basic_preprocess(df):
    """Apply simple Lab01 cleaning steps.

    This function does not do advanced feature engineering. It only prepares a
    cleaner version of the dataset for data understanding and later modeling.
    """
    df = clean_column_names(df)
    df = df.drop_duplicates().copy()

    # Parse possible date columns safely when the column name suggests a date.
    for col in df.columns:
        col_lower = col.lower()
        if "date" in col_lower or col_lower.endswith("_dt"):
            converted = pd.to_datetime(df[col], errors="coerce")
            if converted.notna().sum() > 0:
                df[col] = converted

    # Fill missing values with simple and transparent rules.
    numeric_cols = df.select_dtypes(include="number").columns
    object_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in numeric_cols:
        if df[col].isna().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    for col in object_cols:
        if df[col].isna().sum() > 0:
            mode_values = df[col].mode(dropna=True)
            fill_value = mode_values.iloc[0] if len(mode_values) > 0 else "Unknown"
            df[col] = df[col].fillna(fill_value)
            df[col] = df[col].astype("category")

    return df


def choose_prediction_dataset(cleaned_datasets):
    """Choose the most relevant dataset for readmission prediction.

    A sample submission file can contain a target-like column, but it usually has
    too few feature columns. This function gives it a lower score.
    """
    candidates = []

    for name, df in cleaned_datasets.items():
        target_col = detect_target_column(df)
        if target_col is None:
            continue

        score = df.shape[1] + (df.shape[0] / 10000)
        lowered_name = name.lower()
        if "sample" in lowered_name or "submission" in lowered_name:
            score -= 100

        candidates.append((score, name, target_col))

    if candidates:
        candidates.sort(reverse=True)
        _, selected_name, target_col = candidates[0]
        return selected_name, target_col

    # If no target exists, choose the largest dataset for preparation only.
    selected_name = max(cleaned_datasets, key=lambda key: cleaned_datasets[key].shape[0])
    return selected_name, None
