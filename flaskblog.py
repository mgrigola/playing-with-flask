from flask import Flask, render_template, url_for, flash, redirect, get_flashed_messages
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  # name of the module we're running in (flaskblog)
app.config['SECRET_KEY'] = 'c1b488aabb6759b75c93a0b9987a5112'  #

# temporary data to pass to/read in html templates
postData = [
    {
        'author': 'Author Person 2',
        'title': 'Post title 1',
        'content': 'static content 1',
        'date_created': 'August 13, 2018'
    },
    {
        'author': 'Author Person 2',
        'title': 'Post title 2',
        'content': 'static content 2',
        'date_created': 'August 14, 2018'
    }
]


@app.route("/")
#@app.route("/home")
def page_home():
    return render_template("home.html", posts=postData)  # can't give full path to template?

@app.route("/about")
def page_about():
    return render_template("about.html", title="about")


@app.route("/register", methods=['GET', 'POST'])    # allow GET adn POST requests on this page
def page_register():
    regForm = RegistrationForm()      # creates the form object
    if regForm.validate_on_submit():  # check if form validators passed (see forms.py)
        # popup message indicating success
        flash('Created account: {0}'.format(regForm.userName.data), 'success') # f'Created account: {regForm.userName}'  'Created account '+regForm.userName
        return redirect(url_for('page_home'))  # send new user to home page

    return render_template('register.html', title='register', form=regForm)   # plugs in our code stuff into register.html so it's all html


@app.route("/login", methods=['GET', 'POST'])
def page_login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        if True:
            flash('login successful', 'success')
            return redirect(url_for('page_home'))
        else:
            flash('invalid credentials', 'danger')

    return render_template('login.html', title='login', form=loginForm)


# run script directly
if __name__ == '__main__':
    app.run(debug=True)  # same as FLASK_ENV=development (i think?)
