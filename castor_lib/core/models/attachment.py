"""Path: castor/core/models/attachment.py

This module contains the Pydantic models for the Attachment resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `name`: String
    - `file_name`: String
    - `timestamp`: Date
    - `file_url`: String or Binary data
    - `uploaded_by`: User ID (reference to Users Collection)
    - `notes`: String
"""

from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Attachment(BaseModel):
    """Model for the Attachment resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    name: str
    file_name: str
    timestamp: Optional[datetime] = None
    file_url: str
    uploaded_by: Optional[str] = None
    notes: Optional[str] = None
