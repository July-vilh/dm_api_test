# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run
import time
import uuid
from sqlalchemy.orm import Session

import pytest

from generic.helpers.dm_db import dmDB

from tests.users_table import USERS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from Services.dm_api_account import Facade
import structlog
from generic.helpers.mailhog import mailhog_api

# engine = create_engine(db, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def mailhog():
    return mailhog_api(host='http://5.63.153.31:5025/')


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture
def dm_db():
    db = dmDB(POSTGRES_USER='JULY', POSTGRES_PASSWORD="1356", POSTGRES_DB='JULYdb')
    return db


def test_post_v1_account(dm_api_facade, dm_db):
    # REGISTER NEW USER:
    login = "login000010"
    email = "login000010@mail.ru"
    password = "login_000010"

    dm_api_facade.mailhog.delete_all_messages()

    if not dm_db.user_exists(login, email):
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )


    new_user_info = {
        'Login': login,
        'Email': email,
        'Password': password
    }

    session = Session()
    new_user = USERS(**new_user_info)
    new_user.UserId = str(uuid.uuid4())
    session.add(new_user)
    session.commit()

    dm_db.delete_user_by_login(login=login)
    dataset = dm_db.get_user_by_login(login=login)
    assert len(dataset) == 0

    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f"User {login} not registered"

    # REGISTER ACTIVATE USER:
    dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Status'] is True, f"User {login} not activated"

    # LOGIN USER:
    dm_api_facade.login.login_user(login=login, password=password)

# def check_input_json_request(json):
#     for key, value in json.tems():
#         if key == "login":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "email":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "password":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'


# 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 мой токен шитхаба для пуша (надо настроить права походу)
