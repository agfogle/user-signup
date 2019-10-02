from flask import Flask, request, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def display_form():

    return render_template('index.html')
    


@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    # email = request.signup_form['email']

    # placeholders for errors that I will fill in later
    username_error = ''
    password_error = ''
    verify_error = ''
    # email_error = ''
    # blank_error = ''

    if " " in username:
        username_error = "username can not include spaces"
        
    elif len(username) < 3 or len(username) > 20:
        username_error = "Must be 3 - 20 characters"

    
    if " " in password:
        password_error = "Password can not include spaces"
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = "Must be 3 - 20 characters"    
        password = ''

    if not verify == password:
        verify_error = "Passwords must match"
        password = ''

    #if there is nothing in errors, then that means no errors were found
    if not username_error and not password_error and not verify_error:
        return "Success!"
    else:
        return render_template('index.html', username=username, username_error=username_error, password_error=password_error,
        verify_error=verify_error)
    
# @app.route('/welcome')
# def valid_signup():
#     username = request.args.get('username')


app.run()