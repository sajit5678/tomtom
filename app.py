from flask import Flask, render_template, redirect, url_for, request, session, flash
#from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deducted.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class deducted(db.Model):
	id = db.Column('student_id', db.Integer, primary_key = True)
	date = db.Column(db.String(100))
	name = db.Column(db.String(100))
	city = db.Column(db.String(100))
	addr = db.Column(db.String(200))
	transfer = db.Column(db.String(100))
	bal = db.Column(db.String(100))

	def __init__(self, date, name, city, addr, transfer, bal):
		   self.date = date
		   self.name = name
		   self.city = city
		   self.addr = addr
		   self.transfer = transfer
		   self.bal = bal

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
@login_required
def show_all():
   return render_template('show_all.html', students = deducted.query.all() )

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'najfamily' or request.form['password'] != 'ourfamily':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in. This is my new code')
            return redirect(url_for('show_all'))
    return render_template('login.html', error=error)
	
@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
	if request.method == 'POST':
	  if not request.form['name'] or not request.form['tra']:
		 flash('Please enter all the fields', 'error')
	  else:
		data = deducted.query.all()
		b = request.form['name']
		e = request.form['tra']
		k = request.form['bal']
		j = request.form['date']
		if data:
			for col in data:
				h = col.bal
				g = int(h) + int(e)
		else:
			g = e
			#g = int(h) + int(e)
		deduct = deducted(j, b, '', k, e, g)

		db.session.add(deduct)
		db.session.commit()
		flash('Record was successfully added')
		return redirect(url_for('show_all'))
		
	return render_template('add.html')

@app.route('/use', methods = ['GET', 'POST'])
@login_required
def use():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['deduct']:
         flash('Please enter all the fields', 'error')
      else:
		data = deducted.query.all()
		if data:
			for col in data:
				h = col.bal
		b = request.form['name']
		c = request.form['deduct']
		d = request.form['item']
		j = request.form['date']
		g = int(h)-int(c)
		deduct = deducted(j, b, c, d, '', g)

		db.session.add(deduct)
		db.session.commit()
		flash('Record was successfully added')
		return redirect(url_for('show_all'))
   return render_template('use.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))
	
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)