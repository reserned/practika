from fastapi import FastAPI

from app.api import book_routes, category_routes
from app.db import create_tables


app = FastAPI(
    title="practika book service",
    description="API для учебного каталога книг на FastAPI и PostgreSQL.",
    version="1.0.0",
)


@app.on_event("startup")
def prepare_app() -> None:
    create_tables()


@app.get("/health", tags=["service"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "practika-api",
    }


app.include_router(category_routes.router)
app.include_router(book_routes.router)
