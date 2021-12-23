from flask import Flask, request
# from my_app.bd.models import db
# from my_app.bd import db_funs

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('bd/config.py')
#    db.init_app(app)

    @app.route('/add', methods=['PUT'])
    def add_news():
        print('-- вошли в add_news')
        print('-- вот request.json:\n',request.json)
        return f'вот твой кал --- {request.json}'


    @app.route("/")
    def hello():
        return "Привет!"


    return app


if __name__=="__main__":
    app = create_app()
    app.run(debug=True)