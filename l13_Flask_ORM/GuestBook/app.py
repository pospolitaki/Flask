from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from simple_settings import settings
import json
import itertools

app = Flask(__name__, template_folder='templates')
app.config.update(
    settings.as_dict()
)

db = SQLAlchemy(app)

@app.route('/')
def get_books():
    from models import GuestBookItem
    books = GuestBookItem.query.all()
    return render_template('result.html', books=books)

 

    if request.method == 'POST':
        print(request.form)
        form = GuestBookForm(request.form)
        if form.validate():
            book = GuestBookItem(**form.data)
            db.session.add(book)
            db.session.commit()
    return 'book created!'

@app.route('/price', methods=['GET', 'POST'])
def book_price():
    from forms import PriceForm
    from models import Price, GuestBookItem
    if request.method == 'POST':
        form = PriceForm(request.form)
        print('PriceForm(request.form).data: ', form.data)
        print('request.form:', request.form)
        if form.validate():
            price_book = Price(**form.data)
            db.session.add(price_book)
            db.session.commit()
        return 'you\'ve set the price'
    prices = Price.query.all()
    books = []
    for price in prices:
        book_id = price.guest_book_id
        book = GuestBookItem.query.filter_by(id=book_id).first()
        books.append(book)
    with_price = dict(itertools.zip_longest(books, prices))
    return render_template('result.html', with_price=with_price)

    
    
def main():
    app.run()

if __name__ == '__main__':
    main()