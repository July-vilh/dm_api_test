# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run
import time
from generic.helpers.dm_db import dmDB

db = f"postgresql://JULY:1356@localhost/JULYdb"

from tests.users_table import USERS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from Services.dm_api_account import Facade
import structlog

engine = create_engine(db, echo=True)
Session = sessionmaker(bind=engine)

session = Session()

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')

    # REGISTER NEW USER:
    login = "login000001"
    email = "login000001@mail.ru"
    password = "login_000001"

    db = dmDB(POSTGRES_USER='JULY', POSTGRES_PASSWORD="1356", POSTGRES_DB='JULYdb')

    api.mailhog.delete_all_messages()

    if not db.user_exists(login, email):
        response = api.account.register_new_user(
            login=login,
            email=email,
            password=password
        )

    new_user_info = {
        'login': login,
        'email': email,
        'password': password
    }

    new_user = USERS(**new_user_info)
    session.add(new_user)
    session.commit()

    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['login'] == login, f"User{login}not registered"

    # REGISTER ACTIVATE USER:
    api.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['status'] is True, f"User {login} not activated"

    # LOGIN USER:
    api.login.login_user(login=login, password=password)

# def check_input_json_request(json):
#     for key, value in json.tems():
#         if key == "login":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "email":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'
#         elif key == "password":
#             assert isinstance(value, str), f'Type at the {key} should be str, but now {type(value)}'


# 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 мой токен шитхаба для пуша (надо настроить права походу)
