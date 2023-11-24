from common_libs.db_client.db_client import DBClient


class dmDB:
    def __init__(self, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB):
        self.db = DBClient(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

    def get_sql(self):
        query = 'select * from "information_schema"."sql_features"'
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):
        query = f'''
        select * from "public"."users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        query = '''
          delete from "public"."users"
          where "Login" = '{login}'
          '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    def user_exists(self, login, email):
        # Создаем SQL-запрос для проверки наличия пользователя
        sql = "SELECT COUNT(*) FROM users WHERE \"Login\" = :Login OR \"Email\" = :Email"

        # Параметры для SQL-запроса
        params = {'Login': login, 'Email': email}

        # Выполняем запрос с параметрами
        result = self.db.query(sql, params).scalar()

        # Проверяем, сколько записей было найдено (должно быть 0 или 1)
        return result > 0
