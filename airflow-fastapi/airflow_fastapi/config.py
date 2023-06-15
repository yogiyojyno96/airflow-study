import logging
import os
import base64
from urllib import parse
from typing import List
from pydantic import BaseModel

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

log = logging.getLogger(__name__)

config = Config(".env")

# database
# this will support special chars for credentials
DATABASE_CREDENTIAL_USER = config("DATABASE_CREDENTIAL_USER")
DATABASE_CREDENTIAL_PASSWORD = config("DATABASE_CREDENTIAL_PASSWORD")
DATABASE_HOSTNAME = config("DATABASE_HOSTNAME")
DATABASE_PORT = config("DATABASE_PORT", default="3066")
DATABASE_NAME = config("DATABASE_NAME", default="airflow")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_CREDENTIAL_USER}:{DATABASE_CREDENTIAL_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}?charset=utf8mb4"