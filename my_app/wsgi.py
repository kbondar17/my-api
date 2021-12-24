from my_app.app import app
from bd.models import create_db

if __name__ == '__main__':
    print('стартуем в wsgi')
    create_db()
    app.run(debug=True)