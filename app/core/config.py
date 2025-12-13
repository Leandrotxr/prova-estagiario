from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent

database_url = f"sqlite:///{base_dir / 'app.db'}"