import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from embedded_nn_contracts.tables import regenerate_tables
regenerate_tables(ROOT)
print('tables regenerated')
