"""Path: castor/core/models/tag.py

This module contains the Pydantic models for the Tag resource.

    - `_id`: ObjectId
    - `tag_name`: String
    - `tag_description`: String
    - `tag_color`: String (e.g., "#000000", "#FFFFFF")
    - `user_added`: Boolean
    - `user_id`: ObjectId (reference to Users Collection)
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Tag(BaseModel):
    """Model for the Tag resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    tag_name: str
    tag_description: Optional[str] = None
    tag_color: Optional[str] = None
    user_added: Optional[bool] = None
    user_id: Optional[str] = None
