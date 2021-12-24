from flask import Flask, request
from my_app.bd.models import db
# from bd import db_funs
import logging

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('bd/config.py')
    db.init_app(app)

    @app.route('/add', methods=['PUT'])
    def add_news():
        print('-- вошли в add_news')
        print('-- вот request.json:\n',request.json)
        return f'вот твой кал --- {request.json}'


    @app.route("/")
    def hello():
        logging.warn('логи: послали гет на главную')
        print('послали гет на главную')
        return 'привет'


    return app


app = create_app()
#app.run(debug=True)