# Embedded NN Contracts

Code-only reproducibility toolkit for embedded neural-network deployment
experiments on STM32 microcontrollers and Raspberry Pi edge devices.

## What this project contains

- Frozen CSV/JSON result tables.
- Python validators for canonical values, units, statuses, and Pi5 Vulkan outcomes.
- Scripts to regenerate tables and lightweight SVG figures.
- Tests for metrics, statuses, canonical STM32 values, U575 artifact gates, and secret scanning.
- Safe operator-script templates for optional hardware workloads.

## What this project does not contain

- Vendor runtime binaries.
- Proprietary firmware blobs.
- Raw private server logs.
- Personal paths, SSH settings, board serials, or tokens.
- Non-code document source files.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make validate
make tables
make figures
```

CI validation does not require hardware.

## Validation

Run `make validate` before using regenerated tables or figures.
