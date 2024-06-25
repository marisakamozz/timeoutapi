import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "OK"}


@app.get("/long")
async def take_a_long_time():
    time.sleep(30)
    return {"message": "took a long time"}
