from pathlib import Path

# Raíz del proyecto (asumiendo ejecución desde la raíz)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR      = PROJECT_ROOT / "data"
RAW_DIR       = DATA_DIR / "raw"
INTERIM_DIR   = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR   = PROJECT_ROOT / "reports"
MODELS_DIR    = PROJECT_ROOT / "models"
