from fastapi import FastAPI

from airflow_fastapi.api import api_router

app = FastAPI()

app.include_router(api_router)
