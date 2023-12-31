import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import records
import structlog
from sqlalchemy import text


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class DBClient:
    def __init__(self, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, isolation_level ='AUTOCOMMIT'):
        connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"

        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.db_url = connection_string
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_url(self):
        return self.db_url

    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))

        log.msg(
            event='request',
            query=query
        )

        dataset = self.db.query(query=query).as_dict()

        log.msg(
            event='response',
            dataset=dataset
        )

        return dataset

    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))

        log.msg(
            event='request',
            query=query
        )

        self.db.bulk_query(query=query)

    def execute_query(self, query, **params):
        result = self.db.query(query, **params)
        return result

    def query(self, sql, params):
        try:
            result = self.session.execute(text(sql), params)
            return result
        finally:
            self.session.close()




