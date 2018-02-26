from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def template_practice():
    return render_template('base.html')

name = 'Kirill'
def say_smth(word):
    return word + '!!!'

app.jinja_env.globals.update(name=say_smth)

def main():
    app.run()

if __name__ == '__main__':
    main()