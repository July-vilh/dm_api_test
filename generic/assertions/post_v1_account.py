from hamcrest import assert_that, has_entries


class AssertionsPostV1Account:

    def __int__(self, db):
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
            assert row['Activated'] is True, f'User {login} not activated'
