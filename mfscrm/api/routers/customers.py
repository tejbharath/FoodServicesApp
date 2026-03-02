from fastapi import APIRouter, HTTPException, Depends
from typing import List
from api.schemas import Customer, CustomerCreate, CustomerUpdate, CustomerWithRelations
from api.dependencies import get_django_db
from crm.models import Customer as DjangoCustomer

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)


@router.get("/", response_model=List[Customer])
def get_customers(skip: int = 0, limit: int = 100, db: bool = Depends(get_django_db)):
    """Get all customers"""
    customers = DjangoCustomer.objects.all()[skip:skip + limit]
    return list(customers)


@router.get("/{customer_id}", response_model=CustomerWithRelations)
def get_customer(customer_id: int, db: bool = Depends(get_django_db)):
    """Get a specific customer with their services and products"""
    try:
        customer = DjangoCustomer.objects.prefetch_related('services', 'products').get(id=customer_id)
        return customer
    except DjangoCustomer.DoesNotExist:
        raise HTTPException(status_code=404, detail="Customer not found")


@router.post("/", response_model=Customer, status_code=201)
def create_customer(customer: CustomerCreate, db: bool = Depends(get_django_db)):
    """Create a new customer"""
    db_customer = DjangoCustomer.objects.create(**customer.model_dump())
    return db_customer


@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: CustomerUpdate, db: bool = Depends(get_django_db)):
    """Update a customer"""
    try:
        db_customer = DjangoCustomer.objects.get(id=customer_id)
        update_data = customer.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_customer, field, value)
        db_customer.save()
        return db_customer
    except DjangoCustomer.DoesNotExist:
        raise HTTPException(status_code=404, detail="Customer not found")


@router.delete("/{customer_id}", status_code=204)
def delete_customer(customer_id: int, db: bool = Depends(get_django_db)):
    """Delete a customer"""
    try:
        db_customer = DjangoCustomer.objects.get(id=customer_id)
        db_customer.delete()
        return {"status": "deleted"}
    except DjangoCustomer.DoesNotExist:
        raise HTTPException(status_code=404, detail="Customer not found")
