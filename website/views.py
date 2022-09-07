from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import User, Note, Profile
from . import db
import json

# # For uploading and downloading a file from or to database
# from io import BytesIO
# from flask import send_file

views = Blueprint('views', __name__)

"""
Handle home routes
"""

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
            flash('Note added!', category='success')

    return render_template('home.html', user=current_user)


# Route for deleting a Note
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note was deleted successfully', category='success')

    return jsonify({})


"""
Handle Profile routes
"""

# Route for display the Profile page
@views.route('/profile')
@login_required
def display_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    return render_template('profile.html', user=current_user, profile=profile)


# Route for creating the Profile
@views.route('/create-profile', methods=['GET', 'POST'])
@login_required
def create_profile():
    if request.method == 'POST':
        # Get content from <form> request
        nickname = request.form.get('nickname')
        phone_number = request.form.get('phone_number')
        is_number = phone_number.isnumeric()  # Check if phone number is numeric
        state = request.form.get('state')
        city = request.form.get('city')
        gender = request.form.get('gender')
        user_type = request.form.get('user_type')
        profession = request.form.get('profession')
        addition_details = request.form.get('addition_details')
        img = request.files['profile_image']
        img_name = secure_filename(img.filename)
        # Validation checks
        if len(nickname) < 2:
            flash('Nickname must be at least 2 characters', category='error')
        elif not is_number:
            flash('Phone number must contain digits only', category='error')
        elif len(phone_number) != 10:
            flash('Phone number must be exactly 10 digits', category='error')
        elif not gender:
            flash('Please choose your gender', category='error')
        elif not user_type:
            flash('Please enter your type as a user', category='error')
        # Upload details (replace profile image to the uploaded image)
        else:
            profile_to_add = Profile(nickname=nickname, phone_number=phone_number, state=state,
                                    city=city, gender=gender, user_type=user_type, profession=profession,
                                    addition_details=addition_details, img=img.read(), img_filename=img_name, user_id=current_user.id)
            db.session.add(profile_to_add)
            db.session.commit()
            flash('Your profile has been created', category='success')
            return redirect(url_for('views.display_profile'))

    return render_template('edit_profile.html', user=current_user, profile=None)
 
 
@views.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    profile_db = Profile.query.filter_by(user_id=current_user.id).first()
    if request.method == 'POST':
        img = request.files['profile_image']
        img_name = secure_filename(img.filename)
        profile_db.nickname = request.form.get('nickname')
        profile_db.phone_number = request.form.get('phone_number')
        profile_db.state = request.form.get('state')
        profile_db.city = request.form.get('city')
        profile_db.gender = request.form.get('gender')
        profile_db.user_type = request.form.get('user_type')
        profile_db.profession = request.form.get('profession')
        profile_db.addition_details = request.form.get('addition_details')
        if not img:
            profile_db.img_filename = ''
        else:
            profile_db.img = img.read()
            profile_db.img_filename = img_name
        db.session.commit()
        return redirect(url_for('views.display_profile'))
    return render_template('edit_profile.html', user=current_user, profile=profile_db)



# Route for delete Profile
@views.route('/delete-profile', methods=['POST'])
@login_required
def delete_profile():
    profile_to_delete = json.loads(request.data)
    profile_id = profile_to_delete['profileId']
    profile_to_delete = Profile.query.get(profile_id)
    if profile_to_delete:
        db.session.delete(profile_to_delete)
        db.session.commit()
        flash('Your profile has been deleted successfully from database', category='success')

    return jsonify({})
