from flask import render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Pitches, User

from . import main
from .. import db


@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message= "Hello"
    return render_template('index.html', message=message)

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data


        # Updated pitchinstance
        new_pitch = Pitch(category= category,pitch= pitch)

        title='New Pitch'

        # save review method
        new_pitch.save_pitch()

        return render_template('pitch.html', title=title, pitch_entry= form)