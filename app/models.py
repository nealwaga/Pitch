from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))
    pitches_author = db.Column(db.Integer,db.ForeignKey('pitches.author'))



    def __repr__(self):
        return f'User {self.username}'


class pitches(db.Model):
    __tablename__= 'pitches'
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    time = db.Column(db.String(255))
    users = db.relationship('User',backref = 'pitches',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'        