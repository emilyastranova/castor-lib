"""Path: castor/core/models/user.py

This module contains the Pydantic models for the User resource.
    - `_id`: ObjectId
    - `username`: String
    - `email`: String
    - `first_name`: String
    - `last_name`: String
    - `role`: String (e.g., "Admin", "Manager", "User")
    - `projects`: Array of project IDs
    - `profile_picture`: String or Binary data
    - `preferences`: Array of preference documents
"""
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class User(BaseModel):
    """Model for the User resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    email: Optional[str] = None
    first_name: str
    last_name: str
    role: Optional[str] = None
    projects: Optional[list] = None
    profile_picture: Optional[str] = None
    preferences: Optional[list] = None
