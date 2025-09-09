from typing import List, Dict, Any
from tortoise.exceptions import IntegrityError, DoesNotExist
from app.models import Customer

async def create_customer(data: Dict[str, Any]) -> Customer:
    try:
        customer = await Customer.create(**data)
        return customer
    except IntegrityError as e:
        # typically unique email constraint
        raise

async def get_customer_or_404(customer_id: int) -> Customer:
    try:
        return await Customer.get(id=customer_id)
    except DoesNotExist:
        return None

async def list_customers() -> List[Customer]:
    return await Customer.all().order_by("-created_at")

async def update_customer(customer: Customer, data: Dict[str, Any]) -> Customer:
    for k, v in data.items():
        setattr(customer, k, v)
    await customer.save()
    return customer

async def delete_customer(customer_id: int) -> int:
    deleted = await Customer.filter(id=customer_id).delete()
    return deleted
