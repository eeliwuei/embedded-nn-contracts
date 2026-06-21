from pathlib import Path


INVALID_RUNTIME_TOKENS = ("CM4", "CM7", "M0")
VALID_U575_TOKENS = ("CM33", "U5", "CortexM33", "M33")


def classify_runtime_filename(path: str | Path) -> str:
    name = Path(path).name
    if any(token in name for token in INVALID_RUNTIME_TOKENS):
        return "invalid_runtime_arch"
    if any(token in name for token in VALID_U575_TOKENS):
        return "candidate_requires_readelf_gate"
    return "unknown_runtime_arch"
