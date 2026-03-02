from fastapi import APIRouter, HTTPException, Depends
from typing import List
from api.schemas import Service, ServiceCreate, ServiceUpdate
from api.dependencies import get_django_db
from crm.models import Service as DjangoService

router = APIRouter(
    prefix="/services",
    tags=["services"]
)


@router.get("/", response_model=List[Service])
def get_services(skip: int = 0, limit: int = 100, db: bool = Depends(get_django_db)):
    """Get all services"""
    services = DjangoService.objects.all()[skip:skip + limit]
    return list(services)


@router.get("/{service_id}", response_model=Service)
def get_service(service_id: int, db: bool = Depends(get_django_db)):
    """Get a specific service"""
    try:
        service = DjangoService.objects.get(id=service_id)
        return service
    except DjangoService.DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")


@router.post("/", response_model=Service, status_code=201)
def create_service(service: ServiceCreate, db: bool = Depends(get_django_db)):
    """Create a new service"""
    db_service = DjangoService.objects.create(**service.model_dump())
    return db_service


@router.put("/{service_id}", response_model=Service)
def update_service(service_id: int, service: ServiceUpdate, db: bool = Depends(get_django_db)):
    """Update a service"""
    try:
        db_service = DjangoService.objects.get(id=service_id)
        update_data = service.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_service, field, value)
        db_service.save()
        return db_service
    except DjangoService.DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")


@router.delete("/{service_id}", status_code=204)
def delete_service(service_id: int, db: bool = Depends(get_django_db)):
    """Delete a service"""
    try:
        db_service = DjangoService.objects.get(id=service_id)
        db_service.delete()
        return {"status": "deleted"}
    except DjangoService.DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")
