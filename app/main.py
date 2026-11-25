from fastapi import FastAPI

app = FastAPI(title="FSS API")


@app.get("/health")
def health_check()-> dict[str,str]:
    return {"status":"OK"}