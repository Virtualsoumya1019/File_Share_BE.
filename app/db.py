import os

from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine

def create_db_engine() -> Engine:
    url = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host="127.0.0.1",
        port=5432,
        database="fss",
    )

    return create_engine(
        url,
        pool_pre_ping=True,
        connect_args={"connect_timeout": 5},
    )