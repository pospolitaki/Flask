# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        include = [
            'article_id',
        ]
