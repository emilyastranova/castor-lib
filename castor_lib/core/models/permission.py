"""Path: castor/core/models/client.py

This module contains the Pydantic models for the Client resource.

    - `_id`: ObjectId
    - `permission_name`: String
    - `permission_description`: String
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Permission(BaseModel):
    """Model for the Permission resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    permission_name: str
    permission_description: str
