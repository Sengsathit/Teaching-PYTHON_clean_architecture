from fastapi import FastAPI, Depends
from domain.use_cases import GetProductsUseCase
from di import get_repo

app = FastAPI()

@app.get("/products")
def list_products(repo = Depends(get_repo)):
    get_products_use_case = GetProductsUseCase(repo)
    return get_products_use_case.execute()