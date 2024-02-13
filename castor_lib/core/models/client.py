"""Path: castor/core/models/client.py

This module contains the Pydantic models for the Client resource.

    - `_id`: ObjectId
    - `client_name`: String
    - `client_contacts`: Array of contact Objects
        - `name`: String
        - `email`: String
        - `phone`: String
    - `client_notes`: String
    - `client_logo`: String or Binary data
    - `projects`: Array of project IDs
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Client(BaseModel):
    """Model for the Client resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    client_name: str
    client_contacts: Optional[list] = []
    client_notes: Optional[str] = ""
    client_logo: Optional[str] = None
    projects: Optional[list] = []
