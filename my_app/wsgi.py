from my_app.app import app


if __name__ == '__main__':
    print('стартуем в wsgi')
    app.run(debug=True)