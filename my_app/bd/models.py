#from flask_sqlalchemy import SQLAlchemy
from my_app.bd.my_bd import Base, engine, db_session

from sqlalchemy import Column, Integer, String, DateTime, Time


class News(Base):
    __tablename__ = "test_news_table"
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    url = Column(String, nullable=True)
    source_name = Column(String, nullable=True)
    published = Column(DateTime, nullable=True)

    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'News.title:{self.title}'

#
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
    print('пытаюсь создать базу!!!')
    # Base.metadata.create_all(bind=engine)
    new = News(title = "заааг_2", author = "автоор_2")
    db_session.add(new)
    print('new--', db_session.new)  # напечатать, что нового
    db_session.commit()
    print(News.__table__)
