"""Small utility functions for Lab01."""

from pathlib import Path


def ensure_directories(project_root):
    """Create output directories if they do not exist."""
    project_root = Path(project_root)
    folders = [
        project_root / "data" / "raw",
        project_root / "data" / "processed",
        project_root / "outputs" / "figures",
        project_root / "outputs" / "processed_data",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
