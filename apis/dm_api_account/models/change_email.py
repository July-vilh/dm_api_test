from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, BaseModel, Extra, Field, StrictStr


class ChangeEmail(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = Field(None, description='User login')
    password: Optional[StrictStr] = Field(None, description='User password')
    email: Optional[StrictStr] = Field(None, description='New user email')
