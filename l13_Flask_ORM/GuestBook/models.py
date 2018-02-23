from app import db
from datetime import date

class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    author = db.Column(db.String(80), nullable = False)
    text = db.Column(db.String(3000))
    date = db.Column(db.Date, default=date.today)
    is_deleted = db.Column(db.Boolean, default=False)

    # def __init__(self, author, text):
    #     self.author = author
    #     self.text = text

    def __repr__(self):
        return '''<Author %r>
        <Text %r>
        ''' % (self.author, self.text)
    

