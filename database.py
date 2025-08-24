<<<<<<< HEAD
from sqlalchemy import create_engine, Index, Column, Integer, String, text, insert, select, delete
from sqlalchemy.orm import declarative_base
from settings import db
BaseHomework = declarative_base()
BaseUsers = declarative_base()


class Homework(BaseHomework):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    house_work = Column(String)
    __table_args__ = (Index
                      ('id_homework_tsv',
                       text("to_tsvector('russian', house_work)"),
                       postgresql_using='gin'),)


class Database():
    def __init__(self):
        self.engine = create_engine(db)
        self.homework = Homework.__table__
        self.create_table()

    def create_table(self):
        BaseHomework.metadata.create_all(self.engine)

    def add_homework(self, user_name, house_work):
        with self.engine.begin() as connection:
            add = insert(self.homework).values(
                user_name=user_name,
                house_work=house_work)
            connection.execute(add)

    def search_all(self, username):
        with self.engine.connect() as connection:
            search = select(self.homework.c.id,
                            self.homework.c.user_name,
                            self.homework.c.house_work
                            ).where(self.homework.c.user_name == username)
            result = connection.execute(search)
            return result.fetchall()

    def search_with_user_and_text(self, username, query):
        with self.engine.connect() as connection:
            search = select(
                self.homework.c.id,
                self.homework.c.user_name,
                self.homework.c.house_work).where(
                self.homework.c.user_name == username,
                text("to_tsvector('russian', house_work)@@ plainto_tsquery('russian', :query)")).params(
                query=query)
            result = connection.execute(search)
            return result.fetchall()

    def delete_all(self, username):
        with self.engine.begin() as connection:
            delete_smth = delete(
                self.homework).where(
                self.homework.c.user_name == username)
            connection.execute(delete_smth)

    def close(self):
        self.engine.dispose()
=======
from sqlalchemy import create_engine, Index, Column, Integer, String, text, insert
from sqlalchemy.orm import declarative_base
from settings import db

Base = declarative_base()


class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    house_work = Column(String)
    __table_args__ = (Index
                      ('id_homework_tsv',
                       text("to_tsvector('russian', house_work)"),
                       postgresql_using='gin'),)


class Database():
    def __init__(self):
        self.engine = create_engine(db)
        self.homework = Homework.__table__
        self.create_table()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_homework(self, user_name, house_work):
        with self.engine.begin() as connection:
            add = insert(self.homework).values(
                user_name=user_name,
                house_work=house_work)
            connection.execute(add)

    def search_all(self, username):
        with self.engine.connect() as connection:
            search = text("""
                SELECT id, user_name, house_work
                FROM homework
                WHERE user_name = :username
                """).bindparams(username=username)
            result = connection.execute(search)
            return result.fetchall()

    def search_with_user_and_text(self, username, query):
        with self.engine.connect() as connection:
            search = text("""
                        SELECT id, user_name, house_work
                        FROM homework
                        WHERE user_name = :username
                        AND to_tsvector('russian', house_work)
                        @@ plainto_tsquery('russian', :query)
                       """).bindparams(username=username, query=query)
            result = connection.execute(search)
            return result.fetchall()

    def delete_all(self, username):
        with self.engine.begin() as connection:
            connection.execute(
                text("DELETE FROM homework WHERE user_name = :username").bindparams(username = username))

    def close(self):
        self.engine.dispose()
>>>>>>> a9f594b995eb050cb5db63099ae58e515d2999b4
