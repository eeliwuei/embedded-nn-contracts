#!/usr/bin/env bash
set -euo pipefail
echo "[INFO] Checking local environment for optional hardware workflows."
command -v python3 >/dev/null && echo "[OK] python3 found" || { echo "[ERROR] python3 missing"; exit 1; }
echo "[INFO] Hardware flashing is not run by this script."
