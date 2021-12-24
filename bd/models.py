from flask_sqlalchemy import SQLAlchemy
from bd.my_bd import Base, engine
db = SQLAlchemy()

class News(db.Model):
    __tablename__ = 'test_news_table'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=True)
    author = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    source_name = db.Column(db.String, nullable=True)
    published = db.Column(db.DateTime, nullable=True)

    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'News.title:{self.title}'


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authors = db.Column(db.String, nullable=True)
    rss_sources = db.Column(db.String, nullable=True)


    def __repr__(self): # тут пишем как будет отображатся при печати
        return f'User.id:{self.title}'


def create_db():
    print('в models создаем БД')
    Base.metadata.create_all(bind=engine)

# if __name__ == '__main__': # берем все таблицы и создаем
#     pass