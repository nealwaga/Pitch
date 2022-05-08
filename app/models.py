from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.author}'


class Pitches(db.Model):
    __tablename__= 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    date = db.Column(db.DateTime(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('CommentVote', backref='title', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,cate):
        pitch = Pitches.query.filter_by(category=cate).all()
        return pitch

    def __repr__(self):
        return f"Pitches {self.pitch}','{self.date}')"  


class CommentVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime(250), nullable=False, default=datetime.utcnow)
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"CommentsPost('{self.comment}', '{self.date_posted}')"   