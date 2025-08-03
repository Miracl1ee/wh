from sqlalchemy import create_engine, Index, Table, Column, Integer, String, MetaData, delete, text, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import db  

Base = declarative_base()

class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    house_work = Column(String)
    __table_args__ = (Index('index', text("to_tsvector('russian', house_work)"), postgresql_using='gin'),)

class Database():
    def __init__(self):
        self.engine = create_engine(db)
        self.Session = sessionmaker(bind=self.engine)

    def create_table(self):
        Base.metadata.create_all(self.engine)
            
    def add_homework(self, user_name, house_work):
        with self.engine.connect() as connection:
            add = insert(Homework.__table__)
            for work in house_work:
                add = insert(self.homework).values({'user_name': user_name, 'house_work': work})
                connection.execute(add)
            connection.commit()
    def delete_all(self):
        with self.engine.connect() as connection:
            d = delete(self.homework)
            connection.execute(d)
            connection.commit()
            print('Все данные удалены')
                
    def search_homework(self, query):
        find = text("""SELECT id, user_name, house_work FROM homework 
                        WHERE to_tsvector('russian', house_work) @@ plainto_tsquery('russian', :query)""").bindparams(query=query)
            
        with self.engine.connect() as connection:
            result = connection.execute(find) 
            return result.fetchall()

    def close(self):
        self.engine.dispose()