"""Path: castor/core/models/screenshot.py

This module contains the Pydantic models for the Screenshot resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `task_id`: ObjectId (reference to Tasks Collection)
    - `job_id`: ObjectId (reference to Jobs Collection)
    - `timestamp`: Date
    - `content`: String or Binary data
"""

from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Screenshot(BaseModel):
    """Model for the Screenshot resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    task_id: Optional[str] = None
    job_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    content: str
