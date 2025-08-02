from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, delete, text, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import db  # Убедитесь, что это правильный импорт

Base = declarative_base()

class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    house_work = Column(String)

class Database():
    def __init__(self):
        self.metadata = MetaData()
        
        # Добавим проверку
        if not db:
            raise ValueError("Database URL не настроен!")
            
        self.engine = create_engine(db)
        self.Session = sessionmaker(bind=self.engine)
        self.homework = Table('homework', self.metadata, 
                            Column('id', Integer, primary_key=True), 
                            Column('user_name', String), 
                            Column('house_work', String),
                            extend_existing=True)

    def create_table(self):
        Base.metadata.create_all(self.engine)
            
    def add_homework(self, user_name, house_work):
        with self.engine.connect() as connection:
            for work in house_work:
                stmt = insert(self.homework).values({'user_name': user_name, 'house_work': work})
            connection.execute(stmt)
            connection.commit()
            print('Данные успешно добавлены')

    def delete_all(self):
        with self.engine.connect() as connection:
            stmt = delete(self.homework)
            connection.execute(stmt)
            connection.commit()
            print('Все данные удалены')


    def search_homework(self, query):
    
        with self.engine.connect() as connection:
            stmt = text("""SELECT id, user_name, house_work FROM homework 
                        WHERE house_work ILIKE :query """).bindparams(query=f"%{query}%")
            result = connection.execute(stmt)
            return result.fetchall()
    def close(self):
        self.engine.dispose()