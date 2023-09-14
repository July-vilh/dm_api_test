from pydantic import BaseModel, StrictStr, Field, StrictBool
from enum import Enum
from typing import List, Optional
from datetime import date as Date


class Roles(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = "SeniorModerator"


class Rating(BaseModel):
    enabled: StrictBool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    # medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    # small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    # status: Optional[StrictStr]
    rating: Rating
    # online: Optional[Date]
    # name: Optional[StrictStr]
    # location: Optional[StrictStr]
    # registration: Optional[Date]


class user_envelop(BaseModel):
    resource: User
    # metadata: Optional[StrictStr]

