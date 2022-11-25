# NotesMaster-FullStack-WebApp
## Description
FullStack Web Application, with BackEnd in Flask (Python) and FrontEnd with HTML.
Simple login-signup-logout system.
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

## Home page (access for registered user only)
<img width="953" alt="image" src="https://user-images.githubusercontent.com/58309185/191131704-cbafe2b3-7e42-4618-a2b6-62bd20aa77ea.png">

## Adding a note
<img width="950" alt="image" src="https://user-images.githubusercontent.com/58309185/191131752-a8ce6d36-0735-4f92-8cef-68e8d1cdaa3e.png">

## Profile page (No profile)
<img width="394" alt="image" src="https://user-images.githubusercontent.com/58309185/191131996-3cf6ca76-0e57-4ccc-83ec-2f0b4f13e06f.png">

## Edit profile page
<img width="760" alt="image" src="https://user-images.githubusercontent.com/58309185/191132019-60aa3c1b-a7f9-49d8-9a83-e8c7eaf15716.png">

## Profile page (existing profile)
<img width="374" alt="image" src="https://user-images.githubusercontent.com/58309185/191132159-cf27b17f-4314-41c7-837e-b7c176a192e5.png">

# Running the App - type in CMD:
\env\Scripts\activate <br />
python-m main

# Viewing the App:
Go to URL: http://127.0.0.1:5000
