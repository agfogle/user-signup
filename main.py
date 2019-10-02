from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

@app.route('/')
def display_form():
    return render_template('index.html')
    


@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # placeholders for errors that I will fill in later
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if " " in username:
        username_error = "username can not include spaces"
        
    elif len(username) < 3 or len(username) > 20:
        username_error = "Must be 3 - 20 characters"

    
    if " " in password:
        password_error = "Password can not include spaces"
        password = '' #need to clear out the password so that it does not show
    elif len(password) < 3 or len(password) > 20:
        password_error = "Must be 3 - 20 characters"    
        password = ''

    if not verify == password:
        verify_error = "Passwords must match"
        password = ''

    if not email == "":
        if " " in email:
            email_error = "Email can not include spaces"
        elif len(email) < 3 or len(email) > 20:
            email_error = "Must be 3 - 20 characters"
        elif not (re.search(regex,email)): 
            email_error = "Not a valid email"
        


    #if there is nothing in errors, then that means no errors were found
    if not username_error and not password_error and not verify_error and not email_error:
        return "Success!"
    else:
        return render_template('index.html', username=username, username_error=username_error, password_error=password_error,
        verify_error=verify_error, email=email, email_error=email_error)
    
# @app.route('/welcome')
# def valid_signup():
#     username = request.args.get('username')


app.run()