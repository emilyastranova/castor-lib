"""Path: castor/core/models/comment.py

This module contains the Pydantic models for the Comment resource.
    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `task_id`: ObjectId (reference to Tasks Collection)
    - `timestamp`: Date
    - `user_id`: ObjectId (reference to Users Collection)
    - `content`: String
"""
from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Comment(BaseModel):
    """Model for the Comment resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: Optional[str] = None
    task_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    user_id: str
    content: str
