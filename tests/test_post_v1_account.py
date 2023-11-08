# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run
import time
import uuid
from collections import namedtuple

import pytest
from sqlalchemy.orm import Session
from tests.users_table import USERS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hamcrest import assert_that, has_entries

# Создайте engine (движок) для работы с базой данных
engine = create_engine('postgresql://JULY:1356@localhost/JULYdb')
# Создайте Session класс, связанный с engine
Session = sessionmaker(bind=engine)


@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    user = namedtuple("User", "login, email, password")
    User = user(login="login000017", email="login000017@mail.ru", password="login_000017")
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()

    return User


# @pytest.mark.parametrize('login, email, password', [
#     ('login000019', 'login000019@mail.ru', 'login_000019'),
#     ('loginnnnnnnnnnn', 'loginnnnnnnnnnnnnn@mail.ru', 'loginnnnnnnnnnnnnn'),
#     ('000017777777777777777', '000017777777777777777@mail.ru', '0000177777777777777777'),
#     ('///////////////////////', '////////////////////@mail.ru', '/////////////////////////')
# ])

@pytest.mark.parametrize('login', ['1', '2', '3'])
@pytest.mark.parametrize('email', ['a@mail.ru', '2@mail.com', '//@vvhvhv1.avdv'])
@pytest.mark.parametrize('password', ['1', '2', '3'])
def test_post_v1_account(dm_api_facade, dm_db, login, email, password):
    # REGISTER NEW USER:

    dm_db.delete_user_by_login(login=login)
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

    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                "Login": login
            }
        ))
        # assert row['Login'] == login, f"User {login} not registered"

    # REGISTER ACTIVATE USER:
    dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = dm_db.get_user_by_login(login=login)
    # for row in dataset:
    #     assert_that(row, has_entries(
    #         {
    #             "Status": True
    #         }
    #     ))

        # assert row['Status'] is True, f"User {login} not activated"

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
