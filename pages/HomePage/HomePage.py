from flask import Blueprint, render_template, redirect

HomePage = Blueprint('HomePage', __name__,
                          static_folder='static',
                          template_folder='templates')

#Routes
@HomePage.route('/')
def starting_page():  # put application's code here
    return redirect('/home')

@HomePage.route('/home')
def home_page():  # put application's code here
    return render_template('HomePage.html')