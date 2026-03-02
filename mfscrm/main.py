import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import customers, services, products

# Initialize FastAPI app
app = FastAPI(
    title="MFS CRM API",
    description="FastAPI endpoints for Maverick Food Services CRM",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],  # Django dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(customers.router, prefix="/api")
app.include_router(services.router, prefix="/api")
app.include_router(products.router, prefix="/api")


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "MFS CRM FastAPI",
        "documentation": "/api/docs",
        "endpoints": {
            "customers": "/api/customers",
            "services": "/api/services",
            "products": "/api/products"
        }
    }


@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "MFS CRM API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
