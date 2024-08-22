from fastapi import FastAPI, status

from schemas import NewProduct
from storage import storage

app = FastAPI(
    debug=True,
    title='Group1305'
)


@app.get('/', include_in_schema=False)
def index():
    return {'subject': 'Hello!'}


# CRUD
@app.post('/api/product/', description='create product', status_code=status.HTTP_201_CREATED, tags=['API', 'Product'])
def add_product(new_product: NewProduct) -> dict:
    storage.create_product(new_product)
    return {}
