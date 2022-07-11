from flask import Flask, redirect
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector


app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

## home page
from pages.HomePage.HomePage import HomePage
app.register_blueprint(HomePage)

## working on it
from pages.WorkingOnIt.WorkingOnIt import WorkingOnIt
app.register_blueprint(WorkingOnIt)

## contact
from pages.contact.contact import contact
app.register_blueprint(contact)

employees = {'emp1': {'name': 'Rihanna', 'email': 'reirei@gmail.com', 'nickname': 'RiRi' },
             'emp2': {'name': 'Shakira', 'email': 'myhipsdontlie@gmail.com', 'nickname': 'Shaki'},
             'emp3': {'name': 'Eminem', 'email': '8miles@gmail.com', 'nickname': 'Slim Shady'},
             'emp4': {'name': 'Sia', 'email': 'ponytailROX@gmail.com', 'nickname': 'Si-Ya'}}

emp_dict = {
    'RiRi': '1234',
    'Shaki': '4321',
    'Slim Shady': '1111',
    'Si-Ya': '4444'
}

@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment2_page'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


## assignment_4
from pages.assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)

#----------------------------#
#----DATABASE CONNECTION-----#
#----------------------------#
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='root',
                                       database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


if __name__ == "__main__":
    app.run()