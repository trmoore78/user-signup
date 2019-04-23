from flask import Flask, request,render_template
import cgi
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email =  cgi.escape(request.form['email'])
    emailchain = ".@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    usernameError =""
    passwordError = ""
    password2Error =""
    emailError =""

    periodcount = 0
    spaces = 0
    atsign = 0

    if not username:
        usernameError = "Username is required"
    elif len(username) < 3:
        usernameError = "Username must be at least 3 characters long"
    elif len(username) > 20:
        usernameError = "Username must can be no more than 20 characters long"
   
    if not password:
        passwordError = "Password is required"
    elif len(password) < 3:
        passwordError = "Password must be at least 3 characters long"
    elif len(password) > 20:
        passwordError = "Password must can be no more than 20 characters long"
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError = "Password must contain a number"

    if password2  != password:
        password2Error = "Both password fields must match" 
    elif password2 == "":
        password2Error = "Please enter matching password" 
    elif len(password2) == 1 or password != password2:
        password2Error = "Please enter password that matches previous password"

    
    for char in email:
        if char == ".":
            periodcount += 1

    for char in email:
        if char == "@":
            atsign += 1
    
    for char in email:
        if char == " ":
            spaces += 1

    for char in email:
        if char not in emailchain:
            emailError = "Please enter a valid email"
        elif periodcount == 0 or periodcount > 1:
            emailError = "Please enter a valid email"
        elif atsign == 0 or atsign > 1:
            emailError = "Please enter a valid email"
        elif spaces > 0:
            emailError = "Please enter a valid email"
        elif len(email) < 3 and len(email) >= 1 or len(email) > 20:
            emailError = "Please enter a valid email"            
        elif len(email) == 0:
            emailError = ""
            

    if usernameError or passwordError or password2Error or passwordError or emailError:
        return render_template('index.html',username=username,usernameError = usernameError, password=password,passwordError = passwordError, password2=password2,password2Error = password2Error, email = email,emailError=emailError)
    else:
        return render_template('welcome.html',username=username)

@app.route("/register", methods=['POST'])
def register_page():
    # build the response string
    return render_template('welcome.html')

@app.route("/")
def index():
    return render_template('index.html')


app.run()