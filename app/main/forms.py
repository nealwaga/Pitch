from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

 category = StringField('Choose category',validators=[Required()])

 pitch = TextAreaField('Pitch')

 submit = SubmitField('Submit')