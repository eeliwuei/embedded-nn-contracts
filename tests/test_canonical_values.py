from pathlib import Path
from embedded_nn_contracts.validators import validate_all


def test_canonical_values_pass():
    root = Path(__file__).resolve().parents[1]
    assert validate_all(root) == []
