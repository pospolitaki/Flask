from app import db
from sqlalchemy.orm import relationship
from datetime import date

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    header = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(3000))
    pub_date = db.Column(db.Date, default=date.today())

    # def __init__(self, header, content, pub):
    #     self.header = header
    #     self.content = content
    #     self.pub = pub


    def __repr__(self):
        return '''<Header %r>
        <Content %r>
        ''' % (self.header, self.content)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.Date, default=date.today())
    comment = db.Column(db.String(1000), nullable=False)

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable = False, index=True)
    article = db.relationship('Article', backref=db.backref('comments', lazy='dynamic'), foreign_keys=[article_id, ])

    # def __init__(self, comment, article):
    #     self.comment = comment
    #     self.article_id = article

    def __repr__(self):
        return '''%r <comment %r to_article %r>
        ''' % (self.pub_date, self.comment, self.article.header)