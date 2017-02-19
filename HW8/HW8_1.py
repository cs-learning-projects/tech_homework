# 1.
# По адресу /locales должен возвращаться массив в
# формате json с тремя локалями: ['ru', 'en', 'it']


from flask import Flask
from flask.json import jsonify

app = Flask(__name__)


@app.route('/locales', methods =['GET', 'POST'])
def my_dict():
    my_locale = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(my_locale)


if __name__ == '__main__':
    app.run()
