from flask import Blueprint, render_template

contact = Blueprint('contact', __name__,
                          static_folder='static',
                          template_folder='templates')

#Routes
@contact.route('/contact')
def contact_page():  # put application's code here
    return render_template('contact.html')