"""Path: castor/core/models/role.py

This module contains the Pydantic models for the Role resource.

    - `_id`: ObjectId
    - `role_name`: String
    - `role_permissions`: Array of permission documents
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Role(BaseModel):
    """Model for the Role resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    role_name: str
    role_permissions: Optional[list] = []
