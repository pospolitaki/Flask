# -*- coding: utf-8 -*-

from datetime import date
from myblog import db


class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140), unique=True, nullable=False)
    article_url = db.Column(db.String(350), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)

    def __str__(self):
        return '<Article: {}>'.format(self.title)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer,
                           db.ForeignKey('article.id'),
                           nullable=False,
                           index=True)
    article = db.relationship(Article, foreign_keys=[article_id, ])
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)

    def __str__(self):
        return '<Comment {} to Article: {}>'.format(self.title, self.article.title)
