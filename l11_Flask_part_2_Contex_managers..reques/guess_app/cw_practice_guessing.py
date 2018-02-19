from flask import Flask, request
from wtforms import validators, StringField
from wtforms.fields import IntegerField
from flask_wtf import FlaskForm
import os
from simple_settings import settings
import random

app = Flask(__name__)
app.config.update(
    settings.as_dict()
)

#Forms
class GuessForm(FlaskForm):
    number = IntegerField(validators=[
        validators.InputRequired(),
    ])

#Forms^

random.seed(os.environ['FLASK_RANDOM_SEED'])
def gen_number():
    return random.randint(1,10)
app.config.update(number_to_guess = gen_number())

@app.route('/')
def get_number():
    if request.method == 'GET':
        return 'There is number to guess..'

@app.route('/guess', methods=['POST'])
def guessing_number():
    
    #print(dir(request.form))
    #print('request:', request.form.get('number'))
    if request.method == 'POST':
        form = GuessForm(request.form)
        number_to_guess = app.config.get('number_to_guess')
        users_number = form.number.data
        print('number to guess', number_to_guess)
        if users_number < number_to_guess:
            return 'your number < number to guess'
        elif users_number > number_to_guess:
            return 'your number > number to guess'
        elif users_number == number_to_guess:
            app.config.update(number_to_guess = gen_number())
            return 'Well done, let\'s play again!'

def main():
    app.run()

if __name__ == '__main__':
    main()

