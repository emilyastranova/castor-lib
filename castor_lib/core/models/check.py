"""Path: castor/core/models/check.py

This module contains the Pydantic models for the Check resource.

    - `_id`: ObjectId
    - `id`: String (e.g., "is_nmap_installed")
    - `description`: String
    - `created_by`: String (not a user in the database, this is for the YAML file version control)
    - `tags`: Array of tag IDs (reference to Tags Collection)
    - `command`: String
    - `success_criteria`:
        - `type`: String (e.g., "regex", "string", "boolean", "exit_code")
        - `value`: String
"""

from typing import Optional, Annotated, List
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Check(BaseModel):
    """Model for the Check resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    description: Optional[str] = None
    created_by: Optional[str] = None
    tags: Optional[List[str]] = None
    command: Optional[str] = None
    success_criteria: Optional[dict] = None
