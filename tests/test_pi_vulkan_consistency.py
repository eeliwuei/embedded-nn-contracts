from pathlib import Path
from embedded_nn_contracts.pi_vulkan import validate_pi_vulkan_routes


def test_pi_vulkan_routes():
    root = Path(__file__).resolve().parents[1]
    assert validate_pi_vulkan_routes(root) == []
