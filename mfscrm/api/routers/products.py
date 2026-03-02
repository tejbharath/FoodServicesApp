from fastapi import APIRouter, HTTPException, Depends
from typing import List
from api.schemas import Product, ProductCreate, ProductUpdate
from api.dependencies import get_django_db
from crm.models import Product as DjangoProduct

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/", response_model=List[Product])
def get_products(skip: int = 0, limit: int = 100, db: bool = Depends(get_django_db)):
    """Get all products"""
    products = DjangoProduct.objects.all()[skip:skip + limit]
    return list(products)


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: bool = Depends(get_django_db)):
    """Get a specific product"""
    try:
        product = DjangoProduct.objects.get(id=product_id)
        return product
    except DjangoProduct.DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")


@router.post("/", response_model=Product, status_code=201)
def create_product(product: ProductCreate, db: bool = Depends(get_django_db)):
    """Create a new product"""
    db_product = DjangoProduct.objects.create(**product.model_dump())
    return db_product


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: bool = Depends(get_django_db)):
    """Update a product"""
    try:
        db_product = DjangoProduct.objects.get(id=product_id)
        update_data = product.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_product, field, value)
        db_product.save()
        return db_product
    except DjangoProduct.DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: bool = Depends(get_django_db)):
    """Delete a product"""
    try:
        db_product = DjangoProduct.objects.get(id=product_id)
        db_product.delete()
        return {"status": "deleted"}
    except DjangoProduct.DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")
