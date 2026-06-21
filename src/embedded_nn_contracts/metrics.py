import math


def throughput_to_latency_ms(throughput_inf_sec: float) -> float:
    if throughput_inf_sec <= 0:
        raise ValueError("throughput must be positive")
    return 1000.0 / float(throughput_inf_sec)


def latency_ms_to_fps(latency_ms: float) -> float:
    if latency_ms <= 0:
        raise ValueError("latency must be positive")
    return 1000.0 / float(latency_ms)


def cv_percent(mean: float, sd: float) -> float:
    if mean == 0:
        raise ValueError("mean must be non-zero")
    return abs(float(sd) / float(mean)) * 100.0


def ci95(mean: float, sd: float, n: int) -> tuple[float, float]:
    if n <= 1:
        raise ValueError("n must be greater than 1")
    half_width = 1.96 * float(sd) / math.sqrt(n)
    return float(mean) - half_width, float(mean) + half_width
