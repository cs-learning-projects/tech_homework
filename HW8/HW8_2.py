# 2.
# По адресу /sum/<int:first>/<int:second> должен получать
# в url-адресе два числа, возвращать их сумму

from flask import Flask, request

app = Flask(__name__)


@app.route('/sum/<int:first>/<int:second>')
def calc_sum(first, second):
    return 'sum = {}'.format(first + second)

if __name__ == '__main__':
    app.run()
