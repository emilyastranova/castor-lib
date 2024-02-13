"""Path: castor/core/models/secret.py

This module contains the Pydantic models for the Secret resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `name`: String
    - `type`: String (e.g. "Password", "API Key", "SSH Key", "Certificate")
    - `shared`: Boolean (e.g., true if shared with other users)
    - `username`: String
    - `password`: String
    - `public_key`: String
    - `private_key`: String
    - `certificate`: String
    - `url`: String
    - `notes`: String
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Secret(BaseModel):
    """Model for the Secret resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    name: str
    type: str
    shared: Optional[bool] = False
    username: Optional[str] = None
    password: Optional[str] = None
    public_key: Optional[str] = None
    private_key: Optional[str] = None
    certificate: Optional[str] = None
    url: Optional[str] = None
    notes: Optional[str] = None
