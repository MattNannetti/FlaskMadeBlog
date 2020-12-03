from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


    
posts = [
    {
        'author': 'Matt Nannetti',
        'title': 'Blog post 1',
        'content': 'Blablablabl blabla first',
        'date_posted': 'November 6th, 2020'
    },
    {
        'author': 'Luigi Rigatoni',
        'title': 'Blog post 2',
        'content': 'pasta cooking pizza burning',
        'date_posted': 'November 15th, 2020'
    },
    {
        'author': 'Louis Armstrong',
        'title': 'Blog post 3',
        'content': 'oh yea wake up yea',
        'date_posted': 'November 26th, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accounted created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)