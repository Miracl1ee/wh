from sqlalchemy import create_engine, Column, Integer, String, insert, select
from sqlalchemy.orm import declarative_base
from settings import database_users

BaseUsers = declarative_base()


class User(BaseUsers):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)


class databaseUsers():
    def __init__(self):
        self.engine_users = create_engine(database_users)
        self.users = User.__table__
        self.create_table()

    def create_table(self):
        BaseUsers.metadata.create_all(self.engine_users)

    def register_user(self, username, password_hash):
        with self.engine_users.begin() as connection:
            add = insert(self.users).values(
                user_name=username,
                password_hash=password_hash)
            connection.execute(add)
            return True

    def search_user_by_username(self, username):

        with self.engine_users.connect() as connection:
            search = select(
                self.users.c.id,
                self.users.c.user_name,
                self.users.c.password_hash,
            ).where(self.users.c.user_name == username)
            result = connection.execute(search)
            return result.fetchone()

    def search_by_id(self, id):
        with self.engine_users.connect() as connection:
            search = select(
                self.users.c.id,
                self.users.c.user_name,
                self.users.c.password_hash,
            ).where(self.users.c.id == id)
            result = connection.execute(search)
            return result.fetchone()

    def close(self):
        self.engine_users.dispose()
