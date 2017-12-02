# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World! This is the app develop and design for the \n education purpose only anyone who are interested can contact mamu on the given phone number ok!!!!!!!!!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# # start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)