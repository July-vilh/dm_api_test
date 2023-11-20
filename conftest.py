# import os
#
# import pytest
#
# from generic.assertions.post_v1_account import AssertionsPostV1Account
# from generic.helpers.dm_db import dmDB
# from Services.dm_api_account import Facade
# from vyper import v
# from pathlib import Path
# import structlog
# from generic.helpers.mailhog import mailhog_api
#
# structlog.configure(
#     processors=[
#         structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
#     ]
# )
#
#
# @pytest.fixture
# def mailhog():
#     return mailhog_api(host=v.get('service.mailhog'))
#
#
# @pytest.fixture
# def dm_api_facade(mailhog):
#     return Facade(
#         host=v.get('service.dm_api_account'),
#         mailhog=mailhog
#     )
#
#
# options = (
#     'service.dm_api_account',
#     'service.mailhog',
#     'database.JULYdb.host'
# )
#
#
# @pytest.fixture
# def dm_db():
#     db = dmDB(
#         POSTGRES_USER=v.get('database.JULYdb.POSTGRES_USER'),
#         POSTGRES_PASSWORD=v.get('database.JULYdb.POSTGRES_PASSWORD'),
#         POSTGRES_DB=v.get('database.JULYdb.POSTGRES_DB'),
#         # host=v.get('database.JULYdb.host')
#     )
#     return db
#
# @pytest.fixture
# def assertions(dm_db):
#     return AssertionsPostV1Account(dm_db)
#
# @pytest.fixture(autouse=True)
# def set_config(request):
#     config = Path(__file__).parent.joinpath('config')
#     config_name = request.config.getoption('--env')
#     v.set_config_name(config_name)
#     v.add_config_path(config)
#     v.read_in_config()
#     for option in options:
#         v.set(option, request.config.getoption(f'--{option}'))
#
#
# def pytest_addoption(parser):
#     parser.addoption('--env', action='store', default='stage')
#     for option in options:
#         parser.addoption(f'--{option}', action='store', default=None)