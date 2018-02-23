from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from simple_settings import settings
import json

app = Flask(__name__, template_folder='templates')
app.config.update(
    settings.as_dict()
)

db = SQLAlchemy(app)

@app.route('/')
def get_books():
    from models import GuestBookItem
    books = GuestBookItem.query.all()
    result = []
    for book in books: 
        result.append(str(book))
        print(book)
    return render_template('result.html', books=books)

@app.route('/create', methods=['GET', 'POST'])
def create_book():
    from forms import GuestBookForm
    from models import GuestBookItem

    if request.method == 'POST':
        print(request.form)
        form = GuestBookForm(request.form)
        if form.validate():
            book = GuestBookItem(**form.data)
            db.session.add(book)
            db.session.commit()
    return 'book created!'




def main():
    app.run()

if __name__ == '__main__':
    main()