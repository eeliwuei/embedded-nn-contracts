#!/usr/bin/env bash
set -euo pipefail
column -s, -t < data/frozen_tables/all_board_model_results.csv || cat data/frozen_tables/all_board_model_results.csv
