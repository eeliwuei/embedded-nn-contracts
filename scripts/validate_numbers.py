import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from embedded_nn_contracts.validators import validate_all
from embedded_nn_contracts.pi_vulkan import validate_pi_vulkan_routes

issues = validate_all(ROOT) + validate_pi_vulkan_routes(ROOT)
report = ROOT / "outputs/reports/number_validation.md"
report.parent.mkdir(parents=True, exist_ok=True)
if issues:
    report.write_text("# Number Validation\n\nFAIL\n\n" + "\n".join(f"- {i}" for i in issues) + "\n")
    raise SystemExit("\n".join(issues))
report.write_text("# Number Validation\n\nPASS\n")
print("number validation: PASS")
