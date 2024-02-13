"""Path: castor/core/models/notification.py

This module contains the Pydantic models for the Notification resource.

    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `notification_title`: String
    - `notification_content`: String
    - `notification_timestamp`: Date
    - `notification_read`: Boolean
"""

from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Notification(BaseModel):
    """Model for the Notification resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    notification_title: str
    notification_content: str
    notification_timestamp: Optional[datetime] = None
    notification_read: Optional[bool] = None
