from my_app.server import app

if __name__ == '__main__':
    print('стартуем в wsgi')
    app.run()