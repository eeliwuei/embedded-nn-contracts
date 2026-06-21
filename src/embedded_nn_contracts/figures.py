import csv
from pathlib import Path


def _bar_svg(labels: list[str], values: list[float], title: str) -> str:
    width, height = 760, 420
    max_v = max(values) if values else 1.0
    bars = []
    x0, y0 = 80, 340
    step = 140
    for i, (label, value) in enumerate(zip(labels, values)):
        bar_h = 260 * value / max_v if max_v else 0
        x = x0 + i * step
        y = y0 - bar_h
        bars.append(f'<rect x="{x}" y="{y:.1f}" width="70" height="{bar_h:.1f}" fill="#2f6f9f"/>')
        bars.append(f'<text x="{x+35}" y="365" text-anchor="middle" font-size="13">{label}</text>')
        bars.append(f'<text x="{x+35}" y="{y-8:.1f}" text-anchor="middle" font-size="12">{value:.3g}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
    <rect width="100%" height="100%" fill="white"/>
    <text x="380" y="35" text-anchor="middle" font-size="22" font-family="Arial">{title}</text>
    <line x1="60" y1="340" x2="720" y2="340" stroke="black"/>
    <line x1="60" y1="70" x2="60" y2="340" stroke="black"/>
    {''.join(bars)}
    </svg>'''


def regenerate_figures(root: Path) -> None:
    out = root / "outputs/figures"
    out.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader((root / "data/frozen_tables/all_board_model_results.csv").open()))
    f746 = [r for r in rows if r["board"] == "f746"]
    out.joinpath("f746_throughput.svg").write_text(
        _bar_svg([r["model"].upper() for r in f746], [float(r["throughput_inf_sec"]) for r in f746], "F746 retained throughput"),
        encoding="utf-8",
    )
    pi = list(csv.DictReader((root / "data/frozen_tables/raspberry_pi_supplement_results.csv").open()))
    active = [r for r in pi if r["backend"] == "cpu_or_default" and r["frozen_core_e2e_ms"]]
    out.joinpath("pi5_yolo_latency.svg").write_text(
        _bar_svg([r["model"] for r in active], [float(r["frozen_core_e2e_ms"]) for r in active], "Pi5 YOLO latency"),
        encoding="utf-8",
    )
