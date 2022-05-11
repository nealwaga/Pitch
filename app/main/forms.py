from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
 title = StringField('Pitch Title')
 category = SelectField(u'Pitch Category', choices=[('life', 'life'), ('coding', 'coding'), ('funny', 'funny')])
 pitch = TextAreaField('Pitch')
 submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
