from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime

class Customer(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    phone = fields.CharField(max_length=20, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "customers"

# Pydantic models for FastAPI
Customer_Pydantic = pydantic_model_creator(Customer, name="Customer")
CustomerIn_Pydantic = pydantic_model_creator(Customer, name="CustomerIn", exclude_readonly=True)
