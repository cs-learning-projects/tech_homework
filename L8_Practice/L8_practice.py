'''
 1.
 написать веб сервер, который по адресу /random
 будет отдавать рандомное число
'''

from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/random')
def my_random():
    return str(randint(0, 100))


if __name__ == '__main__':
    app.run()
