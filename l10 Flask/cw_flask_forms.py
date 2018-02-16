from flask_wtf import FlaskForm
from flask import request, Flask
from wtforms import validators, StringField, DateField, ValidationError
import datetime
import json
import os

#VALIDATORS
vacancies = ['IT','Bank', 'HR' ]
new_vac = vacancies.copy()
for i in vacancies:
    new_vac.append(i.casefold())

class ValidData():
    def __init__(self, message=None):
        self.month_now = datetime.datetime.now().month
        if not message:
            message = "Bad"
        self.message = message
    def __call__(self, form, field):
        d = field.data and field.data.month or None 
        print("d",d)
        print("form: ",form.birth_date)
        print("field: ",field)
        
        if d: 
            if d != self.month_now:
                raise ValidationError(self.message)

valid_data = ValidData()
# formatter = lambda values: '::'.join(x for x in vacancies)
class ValidPassword():
    def __init__(self, message=None):
        if not message:
            self.message = 'passwod and password confirmation don\'t match'
        self.message = message

    def __call__(self, form, field):
        # print('field:', field.data)
        # print('form :', form.password)
        # print('True or False: ', form.password.data == form.password_confirm.data )
        p = len(field.data) and field.data or None
        print('p:', p == form.password.data )
        if p and p != form.password.data:
            raise ValidationError(self.message)
        
valid_password = ValidPassword

#^VALIDATORS

class ContolForm(FlaskForm):
    name = StringField(validators=[
        validators.Length(min=4, max=25)
    ])
    
    email = StringField(validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])

    job = StringField(validators=[
        validators.AnyOf(new_vac),
        validators.InputRequired()
    ])
    
    birth_date = DateField(validators=[
        valid_data,
        validators.InputRequired()
    ])

class PasswordForm(FlaskForm):
    email = StringField(validators=[
        validators.InputRequired(),
        validators.Email(),
        validators.Length(min=4, max=35)
    ])
    password = StringField(validators = [
        validators.InputRequired(),
        validators.Length(min=6, max=50),

    ])
    password_confirm = StringField(validators=[
        validators.InputRequired(),
        validators.Length(min=6, max=50),
        valid_password(),
        
    ])



app = Flask(__name__)
app.config.update(
    DEBUG = True,
    WTF_CSRF_ENABLED = False
)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        print("request.form: ",request.form)
        form = ContolForm(request.form)
        print(form.validate())
        if form.validate():
            return('valid', 200)
        else:
            return('invalid', 400)
    if request.method == "GET":
        return 'hello, world', 200

@app.route('/locals')
def locals():
    response = ['ru', 'en', 'it']
    return json.dumps(response)

"""
По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: 
 "status" - 0 или 1 (если ошибка валидации),
 "errors" - список ошибок, если они есть,
 или пустой список.
"""
@app.route('/form/user', methods=["GET", "POST"])
def confirm_password():
    erro = []
    if request.method == "POST":
        try:
            form = PasswordForm(request.form)
            print(form.validate())
        except ValidationError as err:
            erro = err
        if form.validate():
            return('status - {} \n errors : {} '.format(0, erro), 200)
        else:
            return('status - {} \n errors : {} '.format(1, erro), 400)
    # if request.method == "GET":
    #     return 'status - {} \n errors : {} '.format(0, erro), 200

"""
По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.
"""
@app.route('/serve/<path:filename>')
def open_file(filename):
    print('filename >>: ', filename)
    fp = os.path.join('./files',filename)
    if os.path.isfile(fp):
        content = ''
        with open(fp) as file:
            content = file.read()
        return content
    else:
        return 'There is no such file yet (', 404


def main():
    app.run()

if __name__ == '__main__':
    main()
        