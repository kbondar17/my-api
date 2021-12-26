#from flask_sqlalchemy import SQLAlchemy
from my_app.bd.my_bd import Base, engine, db_session
import json
from sqlalchemy import Column, Integer, String, DateTime, Time

class News(Base):
    __tablename__ = "test_news_table"
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    a_id = Column(Integer)
    url = Column(String, nullable=True)
    source_name = Column(String, nullable=True)
    published = Column(DateTime, nullable=True)


    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'News.title:{self.title}'

class Users(Base):
    __tablename__ = "users_table"
    id = Column(Integer, primary_key=True)
    authors = Column(String, nullable=True)
    rss_sources = Column(String, nullable=True)
    notifications = Column(String, nullable=True)

    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'Экземпляр users_table.id:{self.id}'

class Authors(Base):
    __tablename__ = "authors_table"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    source_name = Column(String, nullable=True)

    '''добавить при следующем пересоздании!'''
    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'Экземпляр Authors: {self.name}'



# class Users(db.Model):
#     __tablename__ = "my_users"
#     id = db.Column(db.Integer, primary_key=True)
#     authors = db.Column(db.String, nullable=True)
#     rss_sources = db.Column(db.String, nullable=True)
#
#
#     def __repr__(self): # тут пишем как будет отображатся при печати
#         return f'User.id:{self.title}'



if __name__ == '__main__': # берем все таблицы и создаем

    #
    # print('пытаюсь создать базу!!!')
    # #new = Users(authors = 'афторы', rss_sources = 'ррски', notifications = 'уведомления')
    # db_session.add(new)
    # print('new--', db_session.new)  # напечатать, что нового
    # db_session.commit()
    # print(News.__table__)


    ## удалить таблицу
    Authors.__table__.drop(engine)
    new = Authors(name = "тестовый автор", source_name = "сельская жизнь")
    Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine, tables=[News.__table__])


