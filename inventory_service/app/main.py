from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"service": "inventory", "status": "ok"}
