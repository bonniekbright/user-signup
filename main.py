from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

    
def validate_username(username):
    username, username_error = username, ""
    if username == "":
        username_error = "No username entered."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters."
        username = ""
    elif " " in username:
        username_error = "You can not use a space in the username."
        username = ""
    return username, username_error

def validate_password(password):
    password, password_error = password, ""
    if password == "":
        password_error = "No password entered."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters."
        password = ""
    elif " " in password:
        password_error = "You can not use a space in the password."
        password = ""
    return password, password_error

def validate_verify(verify):
    verify, verify_error = verify, ""
    password = request.form['password']
    if verify == "":
        verify_error = "No verify password was entered"
    elif verify != password:
        verify_error = "Passwords do not match. Reenter password."
        verify = ""
        password = ""
    return verify, verify_error

def validate_email(email):
    email, email_error = email, ""
    if email != "":
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters long."
            email = ""
        elif " " in email:
            email_error = "You can not use a space in the email address."
            email = ""
        elif email.count("@") != 1 or email.count(".") != 1:
            email_error = "Not a valid email address."
    return email, email_error



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/validate", methods=['POST'])
def validate():
    username, username_error = validate_username(request.form["username"])
    password, password_error = validate_password(request.form["password"])
    verify, verify_error = validate_verify(request.form["verify"])
    email, email_error = validate_email(request.form["email"])

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username = username, username_error = username_error, password_error = password_error, 
        verify_error = verify_error, email = email, email_error = email_error)
        

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', title = "welcome", username = username)


app.run()