from pydantic import BaseModel, StrictStr
# from enum import Enum
# from typing import List


class Registrationmodel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr




