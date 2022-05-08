from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):

 category = SelectField(u'Pitch Category', choices=[('life', 'life'), ('coding', 'coding'), ('funny', 'funny')])

 pitch = TextAreaField('Pitch')

 submit = SubmitField('Submit')