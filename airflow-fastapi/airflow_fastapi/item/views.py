from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from airflow_fastapi.item.models import Item

from airflow_fastapi.database.core import get_db

item_router = APIRouter()


@item_router.get("")
def get_item(db:Session = Depends(get_db)):
    return {"test":"test"}


@item_router.post("")
def create_item(db:Session = Depends(get_db) ):
    item = Item(name="test", title="test")
    db.add(item)
    db.commit()
    return {"test":"test"}