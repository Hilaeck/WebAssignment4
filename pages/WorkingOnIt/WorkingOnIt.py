from flask import Blueprint, render_template

WorkingOnIt = Blueprint('WorkingOnIt', __name__,
                          static_folder='static',
                          template_folder='templates')

#Routes
@WorkingOnIt.route('/onProgress')
def working_on_it():  # put application's code here
    return render_template('workingOnIt.html')