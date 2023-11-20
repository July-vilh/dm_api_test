from hamcrest import assert_that, has_entries
from generic.helpers.dm_db import dmDB


class AssertionsPostV1Account:

    def __init__(self, db: dmDB):
        self.db = db

    def check_users_was_created(self, login):
        dataset = self.db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    "Login": login
                }
            ))

    def check_users_was_activated(self, login):
        dataset = self.db.get_user_by_login(login=login)
        for row in dataset:
            assert row['Activated'] is False, f'User {login} not activated'
