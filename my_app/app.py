from flask import Flask, request, 
from my_app.bd import db_funs
import logging

def create_app():
    app = Flask(__name__)

    @app.route('/add', methods=['PUT'])
    def add_news():
        print('-- вошли в add_news')
        print('-- вот request.json:\n',request.json)
        return f'вот твой кал --- {request.json}'

    @app.route('/news', methods=['GET'])
    def get_news():
        news = db_funs.get_latest_news(10)
        return str(news)


    @app.route('/test_add', methods=['PUT'])
    def test_add_news():

        db_funs.add_news([
            {
                'title': 'зааг_3',
                'author': 'аффтор_3',
                'url': 'ссылка_3',
                'source_name': 'имя_3',
                'published': [2021, 12, 1, 1, 1, 1]
            }
        ])

        return 'добавили'

    @app.route("/")
    def hello():
        logging.warn('логи: послали гет на главную')
        print('послали гет на главную')
        return 'привет'


    return app


app = create_app()
#app.run(debug=True)