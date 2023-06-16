from fastapi import APIRouter

item_router = APIRouter()


@item_router.get("")
def get_item():
    return {"test":"test"}


@item_router.post("")
def create_item():
    return {"test":"test"}