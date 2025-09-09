# Customer API (FastAPI + Tortoise ORM + MySQL) — Local development guide

This is a minimal, working example of a REST API for managing customers using:
- FastAPI (backend)
- Tortoise ORM + Aerich (migrations)
- MySQL (database) — you must provide a running MySQL server
- Simple frontend served by FastAPI static files (HTML + JS)

## Quick overview
- Backend code lives in `app/`
- Frontend static files are in `app/frontend/`
- Use the `.env` file to configure DB credentials

## Steps (Windows / Linux)
1. Install Python 3.10+ and MySQL server.
2. Create a Python virtual environment and activate it:
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows (cmd):
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - Linux / macOS:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Install requirements:
```
cd backend
pip install -r requirements.txt
```

4. Create a MySQL database and user (example SQL — run in your MySQL client):
```sql
CREATE DATABASE customerdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'customer_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON customerdb.* TO 'customer_user'@'localhost';
FLUSH PRIVILEGES;
```

5. Copy `.env.example` to `.env` and update credentials:
```
copy .env.example .env   # Windows
cp .env.example .env     # Linux/macOS
```
Edit `.env` and set DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME accordingly.

6. Initialize Aerich (migrations) and create DB schema:
```
# make sure your virtualenv is active and you're in backend folder
# initialize aerich (only first time)
aerich init -t app.tortoise_config.TORTOISE_ORM
# create initial DB structure (reads current models and creates migrations + applies them)
aerich init-db
```

If you later change models:
```
aerich migrate
aerich upgrade
```

7. Run the app:
```
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Open http://127.0.0.1:8000/ to access the frontend UI or http://127.0.0.1:8000/docs for the automatic OpenAPI docs.

## Notes
- Logging writes to `logs/app.log`.
- The Tortoise config is in `app/tortoise_config.py`; it reads from `.env`.
- This example uses `generate_schemas=False` in `register_tortoise` because we use Aerich for migrations.
"# custapi" 
