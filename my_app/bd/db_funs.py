'''тут функции для обращения к БД'''

from my_app.bd.models import News, Authors, db_session
import arrow

def add_news(data:list):
    '''  принимает новости в формате листа словарей вида:
        {
        'title': '',
        'author': '',
        'url': '',
        'source_name':'',
        "publication": ''
        }
    '''
    for article in data:
        # распарсили дату
        # if 'published' in article.keys():
        #     if isinstance(article['published'],list):
        #         published = arrow.get(*article['published'][:-2]).datetime
        #
        #     elif isinstance(article['published'],str):
        #         published = arrow.get(article['published'],'DD MMM YYYY HH:mm:ss').datetime
        #
        # else:
        #     print('неправильный формат даты')
        #     published = arrow.now().datetime
        #
        # проверили, что сочетания ссылка и автор нет в БД. (у одной статьи может быть несколько авторов)
        published = arrow.now().datetime
        existing = News.query.filter(News.url == article['url']).filter(News.author == article['author']).count()
        if not existing:
            # добавили в БД
            new = News(title = article['title'], author=article['author'], a_id = article['a_id'], url=article['url'],
                       source_name=article['source_name'], published = published)
            db_session.add(new)
            db_session.commit()
            print('добавили в БД:', article['title'])
        else:
            print('уже есть---', article['url'])



def get_authors_news(a_id):
    '''получить все новости автора'''
    def get_author_name(a_id):
        name = db_session.query(Authors.name).filter(Authors.id == a_id).all()
        return name
    news = db_session.query(News).filter(News.author == author).all()
    return news


def get_all_authors():
    authors = db_session.query(Authors.name).all()
    return {"res": [{'author':e.name} for e in authors]}


def get_latest_news(how_many = 3):
    '''
    отдает последние новости в виде списка объектов models.News.
    атрибуты (заголовок, ссылка и тд) можно получить через точку.
    '''
    # news = db.session.query(News).order_by(News.published.desc())[:how_many]
    news = db_session.query(News).all()#.order_by(News.published.desc())[:how_many]
    return news

def convert_news(news:News):
    """перевовдит экземлпяры News в словарик"""
    return {'title':news.title, 'author':news.author, 'url' : news.url, 'source_name': news.source_name, 'published': news.published}




if __name__ == "__main__":
    # name = db_session.query(Authors.name).filter(Authors.name == 'Алексей Ковалев').all()
    authors = db_session.query(Authors).all()
    authors_id = {}
    for e in authors:
        authors_id[e.name] = e.id #   'Андрей Колесников': 4


    def parse_dump():
        import json
        from pathlib import Path
        p = Path(__file__).parents[2] / 'main_table_dump.json'

        with open(p, 'r', encoding='utf-8') as f:
            raw = json.load(f)['values']
            to_send = []
            for e in raw:
                to_send.append(
                    {'id': e[0], 'author': e[1], 'a_id': authors_id[e[1]] ,'title': e[2], 'url': e[3], 'published':e[4], 'source_name':e[5]}
                )

            add_news(to_send)

    #parse_dump()
    print(get_all_authors())
    # print(authors_id)

    # def make_authors_table():
    #     authors = db_session.query(News.author, News.source_name ).all()
    #     return set(authors)

    # for e in make_authors_table():
    #         new = Authors(name = e[0].strip(), source_name = e[1].strip())
    #         db_session.add(new)
    #         db_session.commit()


    def recreate_authors():
        # сделать таблциу с авторами
        import json
        from pathlib import Path
        p = Path(__file__).parents[2] / 'main_table_dump.json'
        with open(p, 'r', encoding='utf-8') as f:
            raw = json.load(f)['values']
            to_add = []
            for e in raw:
                pair = [e[1] ,e[-2]]
                if pair not in to_add:
                    to_add.append(pair)

            for e in to_add:
                try:
                    new = Authors(name = e[0], source_name = e[1])
                    db_session.add(new)
                    db_session.commit()

                except Exception as ex:
                    print('----ОШИБКА---',ex)
                    print('---с этим---', e)


