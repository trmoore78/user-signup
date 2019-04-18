from flask import Flask, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-5" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Validation Example</title>
    <link rel="stylesheet" />
  </head>
  <body>
"""

welcomeMessage = """
<h1>Welcome to my registration page!</h1>
<a href="/register" value = "register_form">Site Registration</a> """


page_footer = """
 </body>
</html>
"""

# a registration form
register_form = """
<form action="/register" id="form" method="POST">
      <h1>Register</h1>
      <label for="username">Username</label>
      <input type="text" name="username" id="username" value="{0}" />
      <p class="error">{1}</p>
      <label for="password">Password</label>
      <input type="password" name="password" id="password" value="{2}"/>
      <p class="error">{3}</p>
      <label for="password">Verify Password</label>
      <input type="password" name="password2" id="password2" value="{4}" />
      <p class="error">{5}</p>
      <label for="email">Email(optional)</label>
      <input type="text" name="email" id="email" value="{6}"/>
      <p class="error">{7}</p>
      <button type="submit">Register</button>
    </form>
"""

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email =  cgi.escape(request.form['email'])
    emailchain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.@"

    usernameError =""
    passwordError = ""
    password2Error =""
    emailError =""

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

    if password  != password2:
        password2Error = "Both password fields must match" 
    
    for char in email:
        if char not in emailchain or char == " ":
            emailError = "Please enter a valid email"
        elif len(email) < 3 and len(email) >= 1 or len(email) > 20:
            emailError = "Please enter a valid email"            
        elif len(email) == 0:
            emailError = ""
            

    if usernameError or passwordError or password2Error or passwordError or emailError:
        content = page_header + register_form.format(username, usernameError,"", passwordError, "", password2Error, email,emailError) + page_footer
        return content

    if not usernameError or not passwordError or not password2Error or not passwordError or not emailError:
        noError = "Thank you for registering on my page, "
        content = page_header + noError + username + page_footer
        return content

@app.route("/register", methods=['POST'])
def register_page():
    # build the response string
    content = welcomeMessage + register_form + page_footer
    return content

@app.route("/")
def index():
    return register_form


app.run()