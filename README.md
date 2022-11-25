# NotesMaster-FullStack-WebApp
This is a notes manager website, which stores all user's info (profile is optional) and all notes.
First you need to sign up, then you can add as many notes as you like, and even create your profile card with additional details about yourself. This website is only to practice and enhance my skills in Flask Sever-Side micro framework.

## Technologies
FullStack Web Application, with BackEnd in Flask (Python) and FrontEnd with HTML.
The main branch (name: 'main') is a very basic Web App.
The Flask application is seperated into two Bluprints: auth, views. The first is used for the login, sign-up, logout operations. The second is used for all other requests, like render home page and delete Note from the database.

### For authentication I used several packages
1) werkzeug.security: generate_password_hash, check_password_hash modules.
2) flask_login: login_user, login_required, logout_user, current_user

### Note: All database queries (Create, Update, Delete) are followed by flash messages

## Sign Up page
<img width="763" alt="image" src="https://user-images.githubusercontent.com/58309185/191131610-eb4a48c7-9e0d-47bf-b6b1-cf7807ef4fe4.png">

## Login page
<img width="763" alt="image" src="https://user-images.githubusercontent.com/58309185/191131539-16808d5c-eef1-42c0-a8d1-e33a07116a78.png">

## Home page (access for registered users only)
<img width="953" alt="image" src="https://user-images.githubusercontent.com/58309185/191131704-cbafe2b3-7e42-4618-a2b6-62bd20aa77ea.png">

## Edit profile page
<img width="760" alt="image" src="https://user-images.githubusercontent.com/58309185/191132019-60aa3c1b-a7f9-49d8-9a83-e8c7eaf15716.png">

## Profile page
<img width="374" alt="image" src="https://user-images.githubusercontent.com/58309185/191132159-cf27b17f-4314-41c7-837e-b7c176a192e5.png">

# Running the App - type in CMD:
\env\Scripts\activate <br />
python -m pip install -r requirements.txt <br />
python-m main

# Viewing the App:
Go to URL: http://127.0.0.1:5000
