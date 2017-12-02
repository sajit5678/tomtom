# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
	
# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template
    # return "Hello, World!"  # return a string
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/newpage1')
def newpage1():
    return render_template('main.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            #error = 'Invalid Credentials. Please try again.'
			session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home'))
        else:
            # session['logged_in'] = True
            # flash('You were logged in.')
            # return redirect(url_for('home'))
			error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
   
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))


# # start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
	
	
	
	
	
	
	
	
	
	
	
	
	
# from flask import Flask, render_template

# # create the application object
# app = Flask(__name__)

# # use decorators to link the function to a url
# @app.route('/')
# def home():
    # return "Hello, World! This is the app develop and design for the \n education purpose only anyone who are interested can contact mamu on the given phone number ok!!!!!!!!!"  # return a string

# @app.route('/welcome')
# def welcome():
    # return render_template('welcome.html')  # render a template


# # # start the server with the 'run()' method
# if __name__ == '__main__':
    # app.run(debug=True)