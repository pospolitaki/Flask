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


@app.route('/create_article', methods=['GET', 'POST'])
def create_book():
    from forms import ArticleForm
    from models import Article
    articles = Article.query.all()

    if request.method == 'POST':
        form = ArticleForm(request.form)
        if form.validate():
            print('request.form', request.form)
            print('form', form)
            print('form.data', form.data)
            new_article = Article(**form.data)
            db.session.add(new_article)
            db.session.commit()
            articles = Article.query.all()
            return render_template('article.html', articles=articles)

    return render_template('article.html', articles=articles)

@app.route('/create_comment', methods=['GET', 'POST'])
def create_comment():
    from forms import CommentForm
    from models import Comment
    if request.method == 'POST':
        form = CommentForm(request.form)
        if form.validate():
            new_comment = Comment(**form.data)
            db.session.add(new_comment)
            db.session.commit()
            comments = Comment.query.all()
            return render_template('comments.html', comments=comments)
    comments = Comment.query.all()
    return render_template('comments.html', comments=comments)

@app.route('/')
def start_form():
    return render_template('start_page.html')

def main():
    app.run()

if __name__ == '__main__':
    main()