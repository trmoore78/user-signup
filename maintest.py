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
      <button type="submit">Register</button>
    </form>
"""

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    
    usernameError =""
    
    if not username:
        usernameError = "Username is required"
    elif len(username) < 3:
        usernameError = "Username must be at least 3 characters long"
    elif len(username) > 20:
        usernameError = "Username cannot be more than 20 characters long"
   
    if usernameError:
        content = page_header + register_form.format("", usernameError) + page_footer
       
    elif not usernameError:
        noError = "Thank you for registering on my page"
        content = page_header + noError + username + page_footer

    return content

@app.route("/")
def index():
    return register_form.format("","")


app.run()