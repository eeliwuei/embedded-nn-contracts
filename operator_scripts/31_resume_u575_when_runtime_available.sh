#!/usr/bin/env bash
set -euo pipefail
if [[ "${1:-}" != "--yes" ]]; then
  echo "[ERROR] This optional hardware script requires --yes and a legal U575 runtime bundle."
  exit 2
fi
echo "[INFO] Placeholder resume hook. Use project-specific hardware workspace to build/flash."
