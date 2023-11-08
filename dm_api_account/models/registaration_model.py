from __future__ import annotations
from typing import Optional

from pydantic import ConfigDict, BaseModel, Extra, Field, StrictStr


class Registration(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
    password: Optional[StrictStr] = Field(None, description='Password')




