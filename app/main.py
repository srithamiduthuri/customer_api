import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from app.logging_config import setup_logging
from app.tortoise_config import TORTOISE_ORM

# -------------------------------
# Logging
# -------------------------------
logger = setup_logging()
logger.info("Starting application")

# -------------------------------
# FastAPI app
# -------------------------------
app = FastAPI(title="Customer API (FastAPI + Tortoise ORM)")

# -------------------------------
# CORS middleware (for local testing)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Include routers
# -------------------------------
from app.routers.customers import router as customers_router
app.include_router(customers_router)

# -------------------------------
# Serve frontend static files
# -------------------------------
frontend_dir = Path(__file__).parent / "frontend"
if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
else:
    logger.warning("Frontend directory not found; static files will not be served")

# -------------------------------
# Register Tortoise ORM
# -------------------------------
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Aerich handles migrations
    add_exception_handlers=True,
)

# -------------------------------
# Root route for testing
# -------------------------------
@app.get("/ping")
async def ping():
    return {"message": "Customer API is running"}
