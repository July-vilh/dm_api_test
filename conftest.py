import pytest
from generic.helpers.dm_db import dmDB
from Services.dm_api_account import Facade
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
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture
def dm_db():
    db = dmDB(POSTGRES_USER='JULY', POSTGRES_PASSWORD="1356", POSTGRES_DB='JULYdb')
    return db