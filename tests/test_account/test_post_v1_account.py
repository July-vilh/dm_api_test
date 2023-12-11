# 1. Calling the user registration method (POST)
# Swagger -> import method to the Postman -> choose correct environment (for baseUrl) -> update data in Body (for registration) -> Code -> Python request -> update values in PyCharm and Run

import uuid
from collections import namedtuple
import random
from string import ascii_letters, digits

import allure
import pytest
from sqlalchemy.orm import Session
from tests.users_table import USERS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.post_v1_account import PostV1AccountData as user_data

# Создайте engine (движок) для работы с базой данных
engine = create_engine('postgresql://JULY:1356@localhost/JULYdb')
# Создайте Session класс, связанный с engine
Session = sessionmaker(bind=engine)


def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


@allure.suite("Tests for checking method POST{host}/v1/account")
@allure.sub_suite("Positive checks")
class TestPostV1Account:

    @allure.step("Preparing of test user")
    @pytest.fixture
    def prepare_user(self, dm_api_facade, dm_db):
        user = namedtuple("User", "login, email, password")
        User = user(login=user_data.login, email=user_data.email, password=user_data.password)
        dm_db.delete_user_by_login(login=User.login)
        dataset = dm_db.get_user_by_login(login=User.login)
        assert len(dataset) == 0
        dm_api_facade.mailhog.delete_all_messages()

        return User

    @allure.title("Checking of registration and activation USERS")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertions):
        # REGISTER NEW USER:
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        if not dm_db.user_exists(login, email):
            dm_api_facade.account.register_new_user(
                login=login,
                email=email,
                password=password
            )

        with allure.step("Adding new user at DB"):
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

        assertions.check_users_was_created(login=login)

        # # REGISTER ACTIVATE USER:
        # dm_api_facade.account.activate_registered_user(login=login)
        # # assertions.check_users_was_activated(login=login)
        #
        # # LOGIN USER:
        # dm_api_facade.login.login_user(login=login, password=password)

    @pytest.mark.parametrize('login', [random_string() for _ in range(2)])
    @pytest.mark.parametrize('email', [random_string() + '@mail' + '.ru' for _ in range(2)])
    @pytest.mark.parametrize('password', [random_string() for _ in range(2)])
    def test_create_and_activated_user_with_random_params(self, dm_api_facade, dm_db, login, email, password,
                                                          assertions):
        # REGISTER NEW USER:
        dm_db.delete_user_by_login(login=login)

        dm_api_facade.mailhog.delete_all_messages()

        if not dm_db.user_exists(login, email):
            dm_api_facade.account.register_new_user(
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

            assertions.check_users_was_created(login=login)

            # REGISTER ACTIVATE USER:
            dm_api_facade.account.activate_registered_user(login=login)
            # assertions.check_users_was_activated(login=login)

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
