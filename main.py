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
      <input type="text" name="username" id="username" value="{0}" />
      <p class="error">{1}</p>
      <label for="password">Password</label>
      <input type="password" name="password" id="password" value="{2}" />
      <p class="error">{3}</p>
      <label for="password">Verify Password</label>
      <input type="password" name="password2" id="password2" value="{4}" />
      <p class="error">{5}</p>
      <label for="email">Email(optional)</label>
      <input type="email" name="email" id="email" value="{6}" />
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

    usernameError =""
    passwordError = ""
    password2Error =""
    emailError = ""

    if not username:
        print("no username")
        usernameError = "Username is required"
    if not password:
        passwordError = "Password is required"
    elif len(password) < 5:
        passwordError = "Password must be at least 5 characters long"
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError = "Password must contain a number"
    if password  != password2:
        password2Error = "Password 2 must match password" 

    if usernameError or passwordError or password2Error or passwordError:
        print("there was an error!")
        content = page_header + register_form.format(username, usernameError, 
        password, passwordError, password2, password2Error,email, emailError) + page_footer
        return content

    return "Thanks for registering, " + username


@app.route("/")
def index():
    # build the response string
    content = page_header + welcomeMessage + page_footer
    return content

@app.route("/register", methods=['GET'])
def register_page():
    # build the response string
    content = page_header + register_form.format("", "", "", "", "", "") + page_footer
    return content

app.run()