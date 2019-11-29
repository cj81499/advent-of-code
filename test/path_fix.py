import sys
from pathlib import Path

proj_root = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(proj_root))
sys.path.insert(0, str(proj_root / 'src'))
