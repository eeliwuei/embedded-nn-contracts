import pytest
from embedded_nn_contracts.metrics import throughput_to_latency_ms, latency_ms_to_fps, cv_percent


def test_throughput_to_latency():
    assert throughput_to_latency_ms(396.286) == pytest.approx(2.523, abs=0.001)
    assert throughput_to_latency_ms(8.386) == pytest.approx(119.246, abs=0.01)
    assert throughput_to_latency_ms(0.169) == pytest.approx(5917.159, abs=0.1)


def test_latency_to_fps():
    assert latency_ms_to_fps(71.568197) == pytest.approx(13.973, abs=0.001)


def test_cv_percent():
    assert cv_percent(100.0, 1.0) == pytest.approx(1.0)
