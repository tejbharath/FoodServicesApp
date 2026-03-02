# MFS CRM - Django + FastAPI Integration

This project now includes both **Django** (for web UI) and **FastAPI** (for REST API).

## Architecture

- **Django (Port 8000)**: Handles web interface, templates, authentication, admin panel
- **FastAPI (Port 8001)**: Provides modern REST API endpoints with automatic documentation

## Running the Application

### Option 1: Run both servers automatically
```powershell
cd c:\git\mfscrm\mfscrm
.\start_servers.ps1
```

### Option 2: Run servers separately

**Terminal 1 - Django:**
```powershell
cd c:\git\mfscrm\mfscrm
C:/git/mfscrm/.venv/Scripts/python.exe manage.py runserver
```

**Terminal 2 - FastAPI:**
```powershell
cd c:\git\mfscrm\mfscrm
C:/git/mfscrm/.venv/Scripts/python.exe -m uvicorn main:app --reload --port 8001
```

## Access Points

- **Django Web UI**: http://127.0.0.1:8000
- **FastAPI Root**: http://127.0.0.1:8001
- **API Documentation (Swagger)**: http://127.0.0.1:8001/api/docs
- **API Documentation (ReDoc)**: http://127.0.0.1:8001/api/redoc

## API Endpoints

### Customers
- `GET /api/customers` - List all customers
- `GET /api/customers/{id}` - Get customer with services and products
- `POST /api/customers` - Create new customer
- `PUT /api/customers/{id}` - Update customer
- `DELETE /api/customers/{id}` - Delete customer

### Services
- `GET /api/services` - List all services
- `GET /api/services/{id}` - Get specific service
- `POST /api/services` - Create new service
- `PUT /api/services/{id}` - Update service
- `DELETE /api/services/{id}` - Delete service

### Products
- `GET /api/products` - List all products
- `GET /api/products/{id}` - Get specific product
- `POST /api/products` - Create new product
- `PUT /api/products/{id}` - Update product
- `DELETE /api/products/{id}` - Delete product

## Example API Usage

### Get all customers
```bash
curl http://127.0.0.1:8001/api/customers
```

### Create a customer
```bash
curl -X POST http://127.0.0.1:8001/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "cust_name": "John Doe",
    "organization": "Acme Corp",
    "role": "Manager",
    "email": "john@example.com",
    "bldgroom": "Building A",
    "address": "123 Main St",
    "account_number": 12345,
    "city": "Chicago",
    "state": "IL",
    "zipcode": "60601",
    "phone_number": "555-1234"
  }'
```

## Login Credentials

- **Username**: admin
- **Password**: Iktefak@26

## Benefits of This Architecture

1. **Django** - Mature admin panel, ORM, authentication, templating
2. **FastAPI** - Fast, modern API with automatic OpenAPI docs
3. **Shared Database** - Both use the same Django SQLite database
4. **Type Safety** - Pydantic models ensure data validation
5. **Documentation** - Auto-generated interactive API docs
