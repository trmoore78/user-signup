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
    <link rel="stylesheet" href="/static/app.css" />
  </head>
  <body>
"""

welcomeMessage = """
<h1>Welcome to my super cool page!</h1>
<a href="/register" value = "register_form">Register</a> """


page_footer = """
 </body>
</html>
"""

# a registration form
register_form = """
<form action="/register" id="form" method="POST">
      <h1>Register</h1>
      <label for="username">Username</label>
      <input type="text" name="username" id="username"/>
      <p class="error"></p>
      <label for="password">Password</label>
      <input type="password" name="password" id="password"/>
      <p class="error"></p>
      <label for="password">Verify Password</label>
      <input type="password" name="password2" id="password2" />
      <p class="error"></p>
      <label for="email">Email(optional)</label>
      <input type="text" name="email" id="email" />
      <p class="error"></p>
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
    emailError = ""

    if not username:
        print("no username")
        usernameError = "Username is required"
    elif len(username) < 3:
        passwordError = "Username must be at least 3 characters long"
    elif len(username) > 20:
        passwordError = "Username must can be no more than 20 characters long"
   
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
        password2Error = "Password 2 must match password" 
    
    for char in email:
        if char not in emailchain or char == " ":
            emailError = "Please enter a valid email"
        elif len(email) < 3 or len(email) > 20:
            emailError = "Please enter a valid email"            

    if usernameError or passwordError or password2Error or passwordError or emailError:
        print("there was an error!")
        content = page_header + register_form.format(username, usernameError, 
        password, passwordError, password2, password2Error,email, emailError) + page_footer
        return content



@app.route("/register", methods=['GET'])
def register_page():
    # build the response string
    content = welcomeMessage + register_form + page_footer
    return content

@app.route("/")
def index():
    return register_form.format("")


app.run()