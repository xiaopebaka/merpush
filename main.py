from fastapi import FastAPI
from routers import ProductSearch
app = FastAPI()

app.include_router(ProductSearch.router)

