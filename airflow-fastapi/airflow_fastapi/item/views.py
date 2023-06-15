from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.error_wrappers import ErrorWrapper, ValidationError

from airflow_fastapi.database.core import DbSession

item_router = APIRouter()


@item_router.get("")
def get_item(db_session:DbSession):
    return {"test":"test"}
