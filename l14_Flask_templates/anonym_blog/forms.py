from wtforms_alchemy import ModelForm
from models import Article, Comment

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        include = ['header', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        include = ['article_id','comment']

