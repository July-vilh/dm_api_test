from generic.helpers.orm_db import OrmDB
import structlog
from generic.helpers.orm_models import User


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
    row: User
    for row in dataset:
        print(row.Login)
        print(row.Email)
        print(row.Password)
        print(row.Name)
        print(row.Activated)



    orm.db.close_connection()
