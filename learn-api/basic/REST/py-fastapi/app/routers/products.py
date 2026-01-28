from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["products"],
    # responses is a dictionary of HTTP status codes and their descriptions
    # 404: {"description": "Not found"} means that if the client requests a resource that does not exist, the server will return a 404 status code with the description "Not found".
    # With set 
    responses={404: {"description": "Not found"}},
)

fake_products_db = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"},
    {"id": 3, "name": "Product 3"},
]


@router.get("/")
async def read_products():
    return fake_products_db

@router.get("/{product_id}")
async def read_product(product_id: int):
    for product in fake_products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
