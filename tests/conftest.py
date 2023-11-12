import pytest
from generic.helpers.dm_db import dmDB
from Services.dm_api_account import Facade
from vyper import v
from pathlib import Path
import structlog
from generic.helpers.mailhog import mailhog_api

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def mailhog():
    return mailhog_api(host='http://5.63.153.31:5025/')


@pytest.fixture
def dm_api_facade(mailhog, request):
    host = request.config.getoption('--env')
    return Facade(host=host, mailhog=mailhog)


options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.JULYdb.host'
)


@pytest.fixture
def dm_db():
    db = dmDB(POSTGRES_USER='JULY', POSTGRES_PASSWORD="1356", POSTGRES_DB='JULYdb')
    return db


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stage')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
