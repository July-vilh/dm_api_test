from pydantic import BaseModel, StrictStr, Field
from enum import Enum
from typing import List

Registration_model = {
    "login": "login_8",
    "Email": "login8@mail.ru",
    "Password1": "login_88",
    "roles": ['manager', 'user']
}


class Roles(Enum):
    MANAGER = 'manager'
    USER = 'user'


class Registrationmodel(BaseModel):
    roles: List[Roles]
    login: StrictStr = Field(default='test')
    email: StrictStr = Field(alias="Email", title="email")
    password: StrictStr = Field(min_length=8, alias="Password1", title="password")


print(Registrationmodel(**Registration_model).model_dump_json())

