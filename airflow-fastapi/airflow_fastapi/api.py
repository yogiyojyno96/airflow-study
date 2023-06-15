from fastapi import APIRouter

from airflow_fastapi.item.views import item_router

api_router = APIRouter()

api_router.include_router(item_router, prefix="/items")