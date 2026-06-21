#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "artifacts"
out.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archive = shutil.make_archive(str(out / f"embedded_nn_contracts_private_{stamp}"), "zip", ROOT)
print(archive)
