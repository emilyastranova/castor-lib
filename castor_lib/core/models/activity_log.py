"""Path: castor/core/models/activity_log.py

This module contains the Pydantic models for the Activity Log resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `timestamp`: Date
    - `content`: String
"""

from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ActivityLog(BaseModel):
    """Model for the Activity Log resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    content: str
