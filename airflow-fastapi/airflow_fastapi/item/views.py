from fastapi import APIRouter

from airflow_fastapi.database.core import DbSession
from airflow_fastapi.item.models import Item

item_router = APIRouter()


@item_router.get("")
def get_item(db_session:DbSession):
    return {"test":"test"}


@item_router.post("")
def create_item(db_session:DbSession):
    item = Item(name="test", title="test")
    db_session.add(item)
    db_session.commit()
    return {"test":"test"}