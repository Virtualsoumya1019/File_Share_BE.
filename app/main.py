from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager



from fastapi import FastAPI, HTTPException, Request
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db import create_db_engine

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    engine = create_db_engine()
    app.state.db_engine = engine
    try:
        yield
    finally:
        engine.dispose()


app = FastAPI(title="FSS API", lifespan=lifespan)




@app.get("/health")
def health_check()-> dict[str,str]:
    return {"status":"OK"}

@app.get("/ready")
def ready(request: Request) -> dict[str, str]:
    try:
        with request.app.state.db_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        ) from None

    return {"status": "ready"}