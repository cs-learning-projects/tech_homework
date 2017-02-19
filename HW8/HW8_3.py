# 3.
# По адресу /greet/<user_name> должен получать имя пользователя,
# возвращать текст 'Hello, имя_которое_прислали'

from flask import Flask

app = Flask(__name__)


@app.route('/greet/<user_name>')
def hello_message(user_name):
    return 'Hello, {}!'.format(user_name)

if __name__ == '__main__':
    app.run()
