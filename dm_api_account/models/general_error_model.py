from __future__ import annotations
from typing import Optional

from pydantic import ConfigDict, BaseModel, Extra, Field, StrictStr


class GeneralError(BaseModel):
    model_config = ConfigDict(extra='forbid')

    message: Optional[StrictStr] = Field(None, description='Client message')