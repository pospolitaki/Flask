from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return'Hallo, World!'

@app.route('/test')
def test():
    return'Test!'

def main():
    app.run()

if __name__ == '__main__':
    main()

