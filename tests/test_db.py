from generic.helpers.orm_db import OrmDB
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_orm():
    POSTGRES_USER = 'JULY'
    POSTGRES_PASSWORD = '1356'
    host = 'localhost'
    POSTGRES_DB = 'JULYdb'

    orm = OrmDB(POSTGRES_USER=POSTGRES_USER, POSTGRES_PASSWORD=POSTGRES_PASSWORD, POSTGRES_DB=POSTGRES_DB)

    dataset = orm.get_all_users()

    orm.db.close_connection()
