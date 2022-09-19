<<<<<<< HEAD
# NotesMaster-FullStack-WebApp
FullStack Web Application, with BackEnd in Python (Flask) and FrontEnd with HTML.
I used Jinja templating language for the Web pages.
The main branch (name: 'main') is a very basic Web App. In other branches I will add pages or features like: Profile page, Home page with Images and Animations,
and many other interesting features.

Sign Up page:
<img width="952" alt="image" src="https://user-images.githubusercontent.com/58309185/187580026-03d0bc4f-e18a-4f37-acba-9730af907026.png">

Login page:
![image](https://user-images.githubusercontent.com/58309185/187580153-067c5d3a-bd8c-4017-9e4e-802a481bac4a.png)

Home page (access for registered user only):
![image](https://user-images.githubusercontent.com/58309185/187580472-e4b1796e-596c-4043-8cc5-c6e618fd6d4d.png)

![image](https://user-images.githubusercontent.com/58309185/187580712-0b9108ac-7c47-46de-a0d1-da2024aff9b5.png)

Note: Check the message that is displayed. This is flash messages of Flask - backend module of Python.

To run the application simply run the main.py file:
python main.py

Viewing the App:
Go to URL: http://127.0.0.1:5000
=======
# Description
FullStack Web Application, with BackEnd in Python (Flask) and FrontEnd with HTML.
Simple login-signup-logout system.
The main branch (name: 'main') is a very basic Web App.
The Flask application is seperated into two Bluprints: auth, views. The first is used for the login, sign-up, logout operations. The second is used for all other requests, like render home page and delete Note from the database.

For authentication I used several packages
1) werkzeug.security: generate_password_hash, check_password_hash modules.
2) flask_login: login_user, login_required, logout_user, current_user

All database operations (POST request) are followed by flash messages (from package flask).

# Sign Up page
<img width="952" alt="image" src="https://user-images.githubusercontent.com/58309185/187580026-03d0bc4f-e18a-4f37-acba-9730af907026.png">

# Login page
![image](https://user-images.githubusercontent.com/58309185/187580153-067c5d3a-bd8c-4017-9e4e-802a481bac4a.png)

# Home page (access for registered user only)
![image](https://user-images.githubusercontent.com/58309185/187580472-e4b1796e-596c-4043-8cc5-c6e618fd6d4d.png)

![image](https://user-images.githubusercontent.com/58309185/187580712-0b9108ac-7c47-46de-a0d1-da2024aff9b5.png)

Note: Check the message that is displayed. This is flash messages of Flask - backend module of Python.

# Running the App:
python main.py

# Viewing the App:
Go to URL: http://127.0.0.1:5000
>>>>>>> 2c0eaf93d5e8dfa9a21d2d9aca443cea47fb8e23
