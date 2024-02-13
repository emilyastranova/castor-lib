"""Path: castor/core/models/job.py

This module contains the Pydantic models for the Job resource.
    - `_id`: ObjectId
    - `task_id`: ObjectId (reference to Tasks Collection)
    - `name`: String
    - `description`: String
    - `tags`: Array of tag IDs (reference to Tags Collection)
    - `args`: Object document
    - `command`: ObjectId (reference to Commands Collection)
    - `start_date`: Date
    - `end_date`: Date
    - `duration`: Number (in seconds)
    - `created_by`: User ID (reference to Users Collection)
    - `type`: String (e.g., "Manual", "Automated")
    - `depends_on`: Array of job IDs
    - `status`: String (e.g., "To Do," "In Progress," "Completed")
    - `logs`: Object document
        - `stdin`: String
        - `stdout`: String
        - `stderr`: String
    - `exit_code`: Number
    - `hostname`: String
    - `username`: String
    - `environment_variables`: Array of object documents
        - `name`: String
        - `value`: String
    - `artifacts`: Array of object documents
        - `name`: String
        - `value`: String
    - `screenshots`: Array of screenshot documents
"""

from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Job(BaseModel):
    """Model for the Job resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    task_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    tags: Optional[list] = []
    args: Optional[dict] = {}
    command: Optional[str] = None
    start_date: Optional[datetime] = datetime.now().isoformat()
    end_date: Optional[datetime] = datetime.now().isoformat()
    duration: Optional[float] = 0.0
    created_by: Optional[str] = None
    type: Optional[str] = "Manual"
    depends_on: Optional[list] = []
    status: Optional[str] = "To Do"
    logs: Optional[dict] = {}
    exit_code: Optional[int] = None
    hostname: Optional[str] = None
    username: Optional[str] = None
    environment_variables: Optional[list] = []
    artifacts: Optional[list] = []
    screenshots: Optional[list] = []
