from sqlalchemy import select

from orm_client.orm_client import OrmClient
from generic.helpers.orm_models import User


class OrmDB:
    def __init__(self, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB):
        self.db = OrmClient(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

    def get_all_users(self):
        query = select([User])
        dataset = self.db.send_query(query)
        return dataset
