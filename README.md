# NotesMaster-FullStack-WebApp
## Description
FullStack Web Application, with BackEnd in Python (Flask) and FrontEnd with HTML.
Simple login-signup-logout system.
The main branch (name: 'main') is a very basic Web App.
The Flask application is seperated into two Bluprints: auth, views. The first is used for the login, sign-up, logout operations. The second is used for all other requests, like render home page and delete Note from the database.
### For authentication I used several packages
1) werkzeug.security: generate_password_hash, check_password_hash modules.
2) flask_login: login_user, login_required, logout_user, current_user

## Sign Up page

## Login page

## Home page (access for registered user only)

## Adding a note

## Deleting a note

Note: Check the message that is displayed. This is flash messages (flash module of flask Python)

## Profile page (No profile)

## Edit profile page

## Profile page (existing profile)

# Running the App:
First activate the virtual enviroment by typing (on command line prompt!!):
env\Scripts\activate (and then you should see '(env)' in the start of the new line)
Then run the Web Server by typing:
python -m main

# Viewing the App:
Go to URL: http://127.0.0.1:5000
