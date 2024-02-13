"""Path: castor/core/models/preference.py

This module contains the Pydantic models for the Preference resource.

    - `_id`: ObjectId
    - `user_id`: ObjectId (reference to Users Collection)
    - `theme`: String (e.g., "Dark", "Light")
    - `language`: String (e.g., "English", "Spanish")
    - `timezone`: String (e.g., "America/New_York", "America/Los_Angeles")
    - `notifications`: Boolean
    - `notification_sound`: Boolean
    - `notification_sound_data`: String or Binary data
"""

from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Preference(BaseModel):
    """Model for the Preference resource."""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: Optional[str] = None
    theme: Optional[str] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    notifications: Optional[bool] = None
    notification_sound: Optional[bool] = None
    notification_sound_data: Optional[str] = None
