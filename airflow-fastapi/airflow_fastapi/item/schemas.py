from airflow_fastapi.schemas import BaseSchema, PrimaryKey

class ItemBase(BaseSchema):
    id: PrimaryKey
    name: str
    title: str

