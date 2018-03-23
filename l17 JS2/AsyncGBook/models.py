from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def __str__(self):
        return '((({}))) => {}'.format(self.name, self.message)

    def __repr__(self):
        return '{} \n ___ \n from: {} \n'.format(self.message, self.name)

