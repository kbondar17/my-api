from my_app.bd import db_funs
from flask import Flask,request
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
        content_to_add = request.json
        print('---content_to_add---',content_to_add)
        db_funs.add_news([content_to_add])
        return f'добавили {content_to_add["title"]}'

    @app.route("/")
    def hello():
        logging.warn('логи: послали гет на главную')
        print('послали гет на главную')
        return 'привет'


    return app


app = create_app()
#app.run(debug=True)