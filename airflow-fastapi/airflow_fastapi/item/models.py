from sqlalchemy import (
    Column,
    Integer,
    String,
)

from airflow_fastapi.database.core import Base


class Item(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String, nullable=False)
