'''
2.
- написать route по адресу /submit будет принимать POST запрос, в котором должны быть:
1. Паспортный номер: 10 цифр
2. Имя: Три слова
3. Дата рождения в формате: DD.MM.YYYY
'''

from flask import Flask
from flask import request
from flask_wtf import FlaskForm
from wtforms import IntegerField, ValidationError, StringField, DateField
from wtforms import validators

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'asdasdasd',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})



def pass_number_correct(form, field):
    # print(form, field)
    if len(str(form.data['pass_number'])) != 10:
        raise ValidationError('Passport number should be 10 digits')


class UserForm(FlaskForm):
    pass_number = IntegerField(validators=[pass_number_correct])
    birthday = DateField(format='%d.%m.%Y')
    first_name = StringField(validators=[validators.Length(min=4, max=15)])
    middle_name = StringField(validators=[validators.Length(min=5, max=25)])
    last_name = StringField(validators=[validators.Length(min=4, max=15)])


@app.route('/submit', methods =['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        user_form = UserForm(request.form)

        if user_form.validate():
            print('Паспорт:', request.form['pass_number'])
            print('ФИО:', request.form['first_name'], request.form['middle_name'], request.form['last_name'])
            print('Дата рождения:', request.form['birthday'])
        else:
            print(user_form.errors)
            # как переписать стандартное сообщение об ошибке в дате рождения?
            # где и как сделать ValueError? raise ValueError('Birthday format should by dd.mm.yyy')

    return 'Done!'


if __name__ == '__main__':
    app.run()
