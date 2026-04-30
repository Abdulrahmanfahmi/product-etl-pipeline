
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys
sys.path.insert(0, ".")

from src.extract import extract
from src.transform import transform


_stats = None
_df = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Kör ETL-pipelinen när API:et startar."""
    global _stats, _df
    print("\n=== Kör ETL-pipeline vid API-start ===")
    df_raw = extract("data/products_100.csv")
    _df, _stats = transform(df_raw)
    print("=== API redo ===\n")
    yield


app = FastAPI(
    title="Produkt ETL API",
    description="Exponerar statistik från ETL-pipelinen via REST.",
    version="1.0.0",
    lifespan=lifespan,
)


# Endpoint 1: Full statistik

@app.get("/stats", summary="Full statistik")
def get_stats():
    """Returnerar all statistik från transform-steget."""
    return {
        "total_products": _stats["total_products"],
        "avg_price":      _stats["avg_price"],
        "max_price":      _stats["max_price"],
        "min_price":      _stats["min_price"],
        "total_inventory_value": _stats["total_inventory_value"],
    }


# Endpoint 2: Topp 5 dyraste produkter

@app.get("/top5", summary="Topp 5 dyraste produkter")
def get_top5():
    """Returnerar de 5 dyraste produkterna."""
    return {"top5_expensive": _stats["top5_expensive"]}


# Endpoint 3

@app.get("/categories", summary="Kategoriöversikt")
def get_categories():
    """Returnerar statistik per kategori."""
    return {"categories": _stats["category_summary"]}