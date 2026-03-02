from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from decimal import Decimal


# Customer Schemas
class CustomerBase(BaseModel):
    cust_name: str
    organization: Optional[str] = ""
    role: str
    email: EmailStr
    bldgroom: str
    address: str
    account_number: int
    city: str
    state: str
    zipcode: str
    phone_number: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    cust_name: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    bldgroom: Optional[str] = None
    address: Optional[str] = None
    account_number: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    phone_number: Optional[str] = None


class Customer(CustomerBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True


# Service Schemas
class ServiceBase(BaseModel):
    service_category: str
    description: str
    location: str
    setup_time: datetime
    cleanup_time: datetime
    service_charge: Decimal


class ServiceCreate(ServiceBase):
    cust_name_id: int


class ServiceUpdate(BaseModel):
    service_category: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    setup_time: Optional[datetime] = None
    cleanup_time: Optional[datetime] = None
    service_charge: Optional[Decimal] = None
    cust_name_id: Optional[int] = None


class Service(ServiceBase):
    id: int
    cust_name_id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True


# Product Schemas
class ProductBase(BaseModel):
    product: str
    p_description: str
    quantity: int
    pickup_time: datetime
    charge: Decimal


class ProductCreate(ProductBase):
    cust_name_id: int


class ProductUpdate(BaseModel):
    product: Optional[str] = None
    p_description: Optional[str] = None
    quantity: Optional[int] = None
    pickup_time: Optional[datetime] = None
    charge: Optional[Decimal] = None
    cust_name_id: Optional[int] = None


class Product(ProductBase):
    id: int
    cust_name_id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True


# Response models with relations
class CustomerWithRelations(Customer):
    services: List[Service] = []
    products: List[Product] = []

    class Config:
        from_attributes = True
