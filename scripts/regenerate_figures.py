import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from embedded_nn_contracts.figures import regenerate_figures
regenerate_figures(ROOT)
print('figures regenerated')
