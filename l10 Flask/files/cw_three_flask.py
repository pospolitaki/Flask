from flask import Flask
import os

app = Flask(__name__)

#1. user task
# @app.route('/hello/<name>')
# def hello_user(name):
#     return "hello, dear %s " % name 

# def main():
#     app.run()

#2. two numbers
# @app.route('/')
# def home():
#     return "Welcome to Flask"

# @app.route('/numbers/<first>/<second>')
# def add_numbers(first, second):
#     try:
#         return "{} + {} = {}".format(first, second, int(first) + int(second)) 
#     except (ValueError, TypeError):
#         return "please, make sure you've done correct input"

# @app.route('/')
# def home():
#     return "Welcome to Flask"

# @app.route('/strings/<first>/<second>/<third>')
# def the_longest_str(first, second, third):
#     strings = [first, second, third]
#     le = list(map(len,strings))
#     longest = strings[le.index(max(le))]
    
#     try:
#         return """
#     Your strings: <br>
#     {} <br>
#     {} <br>
#     {} <br>
#     The longest one is:
#     <h1> {} <h1> 
#     """.format(first, second, third, longest) 
#     except (ValueError, TypeError):
#         return "please, make sure you've done correct input"

@app.route('/')
def home():
    return "Welcome to Flask"

@app.route('/file/<path:dir_path>')
def file_exists(dir_path):
    return dir_path
    # if os.path.isfile(dir_path):
    #     return "FILE EXISTS"
    # else:
    #     return "FILE DOESN'T EXIST"

        
def main():
    app.run()


if __name__ == '__main__':
    main()