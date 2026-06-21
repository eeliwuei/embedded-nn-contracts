#!/usr/bin/env bash
set -euo pipefail
RUNTIME_DIR="${U575_RUNTIME_DIR:-}"
if [[ -z "$RUNTIME_DIR" ]]; then
  echo "[INFO] U575_RUNTIME_DIR is not set. U575 source route remains blocked."
  exit 0
fi
echo "[INFO] Checking U575 runtime directory: $RUNTIME_DIR"
find "$RUNTIME_DIR" -name 'NetworkRuntime*CM33*GCC.a' -o -name 'NetworkRuntime*U5*GCC.a' -o -name 'NetworkRuntime*CortexM33*GCC.a'
