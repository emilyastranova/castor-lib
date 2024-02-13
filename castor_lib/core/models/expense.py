"""Path: castor/core/models/expense.py

This module contains the Pydantic models for the Expense resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `name`: String
    - `amount`: Number
    - `date`: Date
    - `notes`: String
"""

from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Expense(BaseModel):
    """Model for the Expense resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    name: str
    amount: float
    date: Optional[datetime] = datetime.now().isoformat()
    notes: Optional[str] = None
