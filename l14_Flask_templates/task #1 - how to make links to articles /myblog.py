# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import date

import config as config


__author__ = 'BorisRubin'


myblog = Flask(__name__, template_folder='templates')
myblog.config.from_object(config)


db = SQLAlchemy(myblog)


@myblog.route('/', methods=['GET', 'POST'])
def index():
    '''
    Основная страница блога, на которой выводится форма для ввода статьи и ниже все введенные статьи
    с возможностью перейти на страницу любой из них

    При создании записи дата ставится текущая
    '''
    if request.method == 'POST':
        form = ArticleForm(request.form)

        if form.validate():
            # так как до первого коммита мы не знаем ID статьи, то сначала коммитим с тем, что
            # в шаблоне по умолчанию 'new', а потом в url подставляем id статьи и коммити еще раз
            article = Article(**form.data)
            db.session.add(article)
            db.session.commit()

            article.article_url = str(article.id)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('errors.html', errors_text=str(form.errors))

    all_articles = Article.query.all()

    return render_template('index.html', articles=all_articles, date_today=date.today())


@myblog.route('/article/<article_url>', methods=['GET', 'POST'])
def new_article(article_url):
    '''
    Страница для вывода конкретной статьи по сгенерированному url
    На этой странице можно добаваить коммент к статье или выйти на главную с помощью кнопок

    При создании комментария дата ставится текущая
    '''
    form = CommentForm(request.form)
    article = Article.query.filter_by(article_url=article_url).first()
    if request.method == 'POST':
        print(request.form)

        if form.validate():
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()
        else:
            return render_template('errors.html', errors_text=str(form.errors))

    all_comments = Comment.query.filter_by(article=article)

    return render_template('article.html', comments=all_comments, article=article, date_today=date.today())
    

if __name__ == '__main__':

    from models import *
    from forms import *

    db.create_all()

    myblog.run()
