from .app import app

if __name__ == '__main__':
    print('стартуем в wsgi')
    app.run()