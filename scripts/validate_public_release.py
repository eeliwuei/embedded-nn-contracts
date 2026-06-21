#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache"}
mac_home = "/" + "Users/"
remote_home = "/" + "home/" + "saop/"
PATTERNS = {
    "mac_home_path": re.compile(re.escape(mac_home)),
    "remote_home_path": re.compile(re.escape(remote_home)),
    "private_key": re.compile(r"BEGIN (?:OPENSSH|RSA|DSA|EC) PRIVATE KEY"),
    "token_like": re.compile(r"(?i)(token|password|secret|api[_-]?key)\s*[:=]\s*[^\s]+"),
    "ssh_real": re.compile(r"ssh\s+[^\n<]*@(?:\d{1,3}\.){3}\d{1,3}"),
}
issues = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.suffix.lower() in {".svg", ".png", ".pdf", ".zip"}:
        continue
    text = path.read_text(errors="ignore")
    for name, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            issues.append(f"{name}: {path.relative_to(ROOT)}:{line}")
            break
report = ROOT / "docs/REDACTION_REPORT.md"
if issues:
    report.write_text("# Redaction Report\n\nFAIL\n\n" + "\n".join(f"- {i}" for i in issues) + "\n")
    raise SystemExit("\n".join(issues))
report.write_text("# Redaction Report\n\nPASS: no high-risk public-release patterns found.\n")
print("public release redaction: PASS")
