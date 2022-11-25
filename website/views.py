from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .forms import ProfileForm
from .models import User, Note
from . import db
import base64
import re


views = Blueprint('views', __name__)


# Route for Adding Notes or get back to Home Web page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has been added!', category='success')

    return render_template('home.html', user=current_user)


# Route for deleting a Note
@views.route('/delete-note/<int:id>')
def delete_note(id):
    note_to_delete = Note.query.filter_by(id=id).first()
    if note_to_delete:
        db.session.delete(note_to_delete)
        db.session.commit()
        flash('Note has been deleted successfully', category='success')
        return redirect(url_for('views.home'))
    return render_template('home.html', user=current_user)


# Route for display the Profile page
@views.route('/profile')
@login_required
def display_profile():
    user = User.query.filter_by(id=current_user.id).first()
    is_profile_exist = True

    img = ''
    if user.img:
        img = base64.b64encode(user.img).decode()
    if not user.nickname and not user.phone_number and not user.state and not user.city  and not user.profession and not user.addition_details:
        is_profile_exist = False

    return render_template('profile.html', user=current_user, img=img, is_profile_exist=is_profile_exist)
 
 
@views.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = ProfileForm()
    user = User.query.filter_by(id=current_user.id).first()

    if form.validate_on_submit():  # POST request
        user.nickname = form.nickname.data
        user.phone_number = form.phone_number.data
        user.state = form.state.data
        user.city = form.city.data
        user.gender = form.gender.data
        user.user_type = form.user_type.data
        user.profession = form.profession.data
        user.addition_details = form.addition_details.data
        img = form.img.data
        
        # Regular expression for phone number

        ## Validations
        # Phone number
        if len(form.phone_number.data) != 10:
            flash('Phone number must be exactly 10 digits', category='error')
            return redirect(url_for('views.update_profile'))
        
        # Image
        elif not img:
            user.img_filename, user.img = None, None
        ## Correct - add to database
        else:
            user.img, user.img_filename = form.img.data.read(), secure_filename(img.filename)
        db.session.commit()  # Update changes to database
        flash('Your profile has been updated successfully', category='success')
        return redirect(url_for('views.display_profile'))

    return render_template('edit_profile.html', user=user, form=form)


@views.route('/delete-profile')
@login_required
def delete_profile():
    user = User.query.filter_by(id=current_user.id).first()
    user.nickname = None
    user.phone_number = None
    user.state = None
    user.city = None
    user.gender = None
    user.user_type = None
    user.profession = None
    user.addition_details = None
    user.img = None
    user.img_filename = None
    db.session.commit()
    flash('Profile has been deleted successfully', category='success')
    return redirect(url_for('views.display_profile'))
