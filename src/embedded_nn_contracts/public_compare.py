from pathlib import Path


def public_matrix_path(root: Path) -> Path:
    return root / 'data/frozen_tables/mlperf_public_results_matrix.csv'
