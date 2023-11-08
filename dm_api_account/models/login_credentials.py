from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, BaseModel, Extra, Field, StrictStr


class LoginCredentials(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
