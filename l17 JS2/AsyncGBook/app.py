from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, make_response, current_app, Flask, request, render_template, redirect, url_for, jsonify
from simple_settings import settings
from datetime import timedelta
import six
from functools import update_wrapper

app = Flask(__name__, template_folder='templates')
app.config.update(
settings.as_dict()
)
db = SQLAlchemy(app)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, six.string_types):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, six.string_types):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
def home_page():
    from models import Message
    messages = Message.query.all()
    return render_template('home.html', messages=messages)

    

@app.route('/comment/', methods=['POST', 'GET'])
@crossdomain('*')
def comment():
    from models import Message
    from forms import MessageForm 
    if request.method == 'POST':
        form = MessageForm(request.form)
        print('request.form =>', request.form)
        print('form =>', form)
        print('form.data =>', form.data)
        
        if form.validate():
            new_message = Message(**form.data)
            db.session.add(new_message)
            db.session.commit()
    return jsonify('Success!')
            

def main():
    
    app.run()

if __name__ == '__main__':
    main()
