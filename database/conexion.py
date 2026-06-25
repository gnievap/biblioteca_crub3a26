import os
import psycopg2  # type: ignore[import]

from pathlib import Path


def load_dotenv():
    env_path = Path('.') / '.env'
    if not env_path.exists():
        return

    with env_path.open(encoding='utf-8') as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


load_dotenv()

class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )