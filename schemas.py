"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection. The collection name
is the lowercase class name (e.g., Contact -> "contact").
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contact(BaseModel):
    """
    Contact messages submitted from the portfolio site.
    Collection: "contact"
    """
    name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)
    source: Optional[str] = Field(None, description="Where the message came from (e.g., portfolio form)")

# Example schemas (kept for reference/testing)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
