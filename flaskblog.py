from flask import Flask, render_template
app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)
