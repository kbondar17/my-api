from my_app.bd import db_funs
from flask import Flask,request
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

    def row_as_dict(query_row):
        return {column.key: str(getattr(query_row, column.key))
                for column in inspect(query_row).mapper.column_attrs}

    def query_as_json(query_result):
        try:
            return json.dumps(row_as_dict(query_result))
        except (AttributeError, TypeError):
            final_list = []
            for q in query_result:
                final_list.append(row_as_dict(q))
            return json.dumps(final_list)

    @app.route('/news', methods=['GET'])
    def get_news():
        news = db_funs.get_latest_news(10)
        return query_as_json(news)


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