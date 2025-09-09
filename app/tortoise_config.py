import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()  # loads .env file if present

DB_USER = os.getenv("DB_USER", "root")
DB_PASS = quote_plus(os.getenv("DB_PASS", "Ak68@2002"))  # encode special chars
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "custapi")

DB_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TORTOISE_ORM = {
    "connections": {
        "default": DB_URL
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # include aerich.models for migrations
            "default_connection": "default",
        }
    },
}
