from my_app.bd import db_funs
from flask import Flask, request, jsonify
import logging
import json
from sqlalchemy import desc, inspect

def create_app():
    app = Flask(__name__)

    # @app.route('/add', methods=['PUT'])
    # def add_news():
    #     print('-- вошли в add_news')
    #     print('-- вот request.json:\n',request.json)
    #     return f'вот твой кал --- {request.json}'



    @app.route('/news', methods=['GET'])
    def get_news():
        data = db_funs.get_latest_news()
        if data:
            return { 'news' : [db_funs.convert_news(e) for e in data] }
        return 'новостей нет'

    @app.route('/authors', methods=['GET'])
    def get_all_authors():
        return db_funs.get_all_authors()

    @app.route('/news/<int:author_id>', methods=['GET'])
    def get_news_of_author():
        '''айди-имя'''
        author_id = ''


    @app.route('/add', methods=['PUT'])
    def test_add_news():
        content_to_add = request.json
        db_funs.add_news(content_to_add)
        titles = [e["title"] for e in content_to_add]
        return f'добавили {str(titles)}'


    @app.route("/")
    def hello():
        logging.warn('логи: послали гет на главную')
        print('послали гет на главную')
        return 'привет'


    return app


app = create_app()
#app.run(debug=True)