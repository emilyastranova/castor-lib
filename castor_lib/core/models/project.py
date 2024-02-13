"""Path: castor/core/models/project.py

This module contains the Pydantic models for the Project resource.

    - `_id`: ObjectId
    - `codename`: String (e.g. MPR23-101)
    - `project_name`: String
    - `client_id`: ObjectId (reference to Clients Collection)
    - `start_date`: Date
    - `end_date`: Date
    - `type`: String (e.g. "External", "Red Team", "Purple Team", "Custom")
    - `tasks`: Array of task IDs
    - `users`: Array of user IDs (reference to Users Collection)
    - `notes`: String
    - `comments`: Array of comment documents
    - `screenshots`: Array of screenshot documents
    - `attachments`: Array of attachment documents
    - `budget`: Number
    - `expenses`: Array of expense documents
    - `activity_logs`: Array of activity log documents
    - `secrets`: Array of secrets documents
    - `created_by`: User ID (reference to Users Collection)
    - `bookmarks`: Array of URL objects
        - `name`: String
        - `url`: String
"""

from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Project(BaseModel):
    """Model for the Project resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    codename: Optional[str] = None
    project_name: str
    client_id: Optional[str] = None
    start_date: Optional[datetime] = datetime.now().isoformat()
    end_date: Optional[datetime] = datetime.now().isoformat()
    type: Optional[str] = "External"
    tasks: Optional[list] = []
    users: Optional[list] = []
    notes: Optional[str] = ""
    comments: Optional[list] = []
    screenshots: Optional[list] = []
    attachments: Optional[list] = []
    budget: Optional[float] = 0.0
    expenses: Optional[list] = []
    activity_logs: Optional[list] = []
    secrets: Optional[list] = []
    created_by: Optional[str] = None
    bookmarks: Optional[list] = []
