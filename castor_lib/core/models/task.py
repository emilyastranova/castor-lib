"""Path: castor/core/models/task.py

This module contains the Pydantic models for the Task resource.
    - `_id`: ObjectId
    - `project_id`: String (reference to Projects Collection)
    - `title`: String
    - `description`: String
    - `created_at`: Date
    - `updated_at`: Date
    - `created_by`: User ID (reference to Users Collection)
    - `type`: String (e.g., "Manual", "Automated")
    - `depends_on`: Array of task IDs
    - `tasks`: Array of task documents
    - `parent_task`: Task ID (reference to Tasks Collection)
    - `assigned_to`: Array of user IDs (reference to Users Collection)
    - `tags`: Array of tag IDs (reference to Tags Collection)
    - `priority`: Number (e.g., 0 for none, 1 for low, 2 for medium, 3 for high)
    - `jobs`: Array of job documents
    - `status`: String (e.g., "To Do," "In Progress," "Completed")
    - `comments`: Array of comment documents
    - `screenshots`: Array of screenshot documents
"""

from typing import Optional, Annotated
from datetime import datetime
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Task(BaseModel):
    """Model for the Task resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    project_id: str
    title: str
    description: Optional[str] = None
    created_at: Optional[str] = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()
    created_by: Optional[str] = None
    type: Optional[str] = "Manual"
    depends_on: Optional[list] = []
    tasks: Optional[list] = []
    parent_task: Optional[str] = None
    assigned_to: Optional[list] = []
    tags: Optional[list] = []
    priority: Optional[int] = 0
    jobs: Optional[list] = []
    status: Optional[str] = "To Do"
    comments: Optional[list] = []
    screenshots: Optional[list] = []
