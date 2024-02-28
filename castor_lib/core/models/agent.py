"""Path: castor/core/models/agent.py

This module contains the Pydantic models for the Agent resource.
    - `_id`: ObjectId
    - `agent_hostname`: String
    - `agent_os`: String (e.g., "Windows", "Linux", "Mac", "Docker", "Kubernetes")
    - `agent_websocket_id`: String
    - `agent_username`: String
    - `agent_status`: String (e.g., "Online", "Offline", "Busy", "Idle")
    - `agent_logs`: Array of log documents
    - `agent_jobs`: Array of job documents
    - `agent_tags`: Array of tag documents
    - `agent_preferences`: Array of preference documents
    - `agent_activity_logs`: Array of activity log documents
    - `agent_secrets`: Array of secrets documents
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Agent(BaseModel):
    """Model for the Agent resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    hostname: Optional[str] = None
    os: Optional[str] = None
    username: Optional[str] = None
    websocket_id: Optional[str] = None
    status: Optional[str] = "Unknown"
    logs: Optional[list] = "No logs available"
    jobs: Optional[list] = []
    agent_tags: Optional[list] = []
    agent_preferences: Optional[list] = []
    activity_logs: Optional[list] = []
    secrets: Optional[list] = []
