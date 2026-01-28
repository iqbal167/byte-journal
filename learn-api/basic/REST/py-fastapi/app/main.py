from fastapi import Depends, FastAPI

from .routers import products

app = FastAPI()

app.include_router(products.router)

@app.get("/")
async def read_root():
    return {"message": "Hello from py-fastapi!"}