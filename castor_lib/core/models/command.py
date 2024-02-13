"""Path: castor/core/models/command.py

This module contains the Pydantic models for the Command resource.

    - `_id`: ObjectId
    - `id`: String (e.g., "nmap")
    - `schema_version`: Number
    - `description`: String
    - `created_by`: String (not a user in the database, this is for the YAML file version control)
    - `checks`: Array of check documents (reference to Checks Collection)
    - `tags`: Array of tag IDs (reference to Tags Collection)
    - `args`: Array of argument documents
    - `command`: String
"""

from typing import Optional, Annotated, List
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Argument(BaseModel):
    """Model for the Argument sub-document."""
    arg_name: str
    arg_description: Optional[str] = None
    arg_required: Optional[bool] = None
    arg_default: Optional[str] = None
    arg_example: Optional[str] = None
    arg_type: Optional[str] = None
    arg_choices: Optional[List[str]] = None

class Command(BaseModel):
    """Model for the Command resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    schema_version: Optional[float] = None
    description: Optional[str] = None
    created_by: Optional[str] = None
    checks: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    args: Optional[List[Argument]] = None
    command: Optional[str] = None
