from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '54cb0a1257b1585952f7ea15492dc6fa'

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

@app.route('/login')
def login():
    form = LoginForm
    return render_template('login.html', tilte='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accounted created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
