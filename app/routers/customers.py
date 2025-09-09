from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Customer, Customer_Pydantic, CustomerIn_Pydantic

router = APIRouter(prefix="/api/customers", tags=["customers"])

# -------------------------------
# Create Customer
# -------------------------------
@router.post("/", response_model=Customer_Pydantic, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerIn_Pydantic):
    try:
        obj = await Customer.create(**customer.dict())
        return await Customer_Pydantic.from_tortoise_orm(obj)
    except Exception as e:
        # Check if email is duplicate (assuming unique constraint)
        raise HTTPException(status_code=400, detail=str(e))

# -------------------------------
# List All Customers
# -------------------------------
@router.get("/", response_model=List[Customer_Pydantic])
@router.get("", response_model=List[Customer_Pydantic])  # no trailing slash
async def list_customers():
    return await Customer_Pydantic.from_queryset(Customer.all().order_by("-created_at"))

# -------------------------------
# Get Single Customer
# -------------------------------
@router.get("/{customer_id}", response_model=Customer_Pydantic)
async def get_customer(customer_id: int):
    obj = await Customer.get_or_none(id=customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    return await Customer_Pydantic.from_tortoise_orm(obj)

# -------------------------------
# Update Customer
# -------------------------------
@router.put("/{customer_id}", response_model=Customer_Pydantic)
async def update_customer(customer_id: int, payload: CustomerIn_Pydantic):
    obj = await Customer.get_or_none(id=customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    data = payload.dict(exclude_unset=True)
    
    # Optional: check for email uniqueness
    if "email" in data:
        existing = await Customer.filter(email=data["email"]).exclude(id=customer_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    for key, value in data.items():
        setattr(obj, key, value)
    await obj.save()
    return await Customer_Pydantic.from_tortoise_orm(obj)

# -------------------------------
# Delete Customer
# -------------------------------
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int):
    deleted = await Customer.filter(id=customer_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None
