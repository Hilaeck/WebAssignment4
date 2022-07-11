from flask import Blueprint, render_template, request, jsonify
import mysql.connector
import requests

assignment_4 = Blueprint('assignment_4', __name__,
                          static_folder='static',
                          template_folder='templates')

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

#Routes
@assignment_4.route('/assignment_4')
def assignment_4_page():  # put application's code here
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', employees = employees_list)

@assignment_4.route('/assignment_4/insertEmp', methods=['GET', 'POST'])
def index():
    name = request.form['name']
    email = request.form['email']
    nickname = request.form['nickname']
    password = request.form['password']
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    for emp in employees_list:
        if name == emp.name:
            return render_template('assignment_4.html', employees=employees_list)
    query = "INSERT INTO employees(name, email, nickname, password) VALUES ('%s','%s', '%s', '%s')" % (name, email, nickname, password)
    interact_db(query=query, query_type='commit')
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', employees=employees_list, message="Employee inserted!")

@assignment_4.route('/assignment_4/updateEmp', methods=['GET', 'POST'])
def update_emp():
    name = request.form['name']
    email = request.form['email']
    nickname = request.form['nickname']
    password = request.form['password']
    query = "UPDATE employees SET name ='%s',nickname ='%s',password='%s' WHERE email='%s';" % (
        name, nickname, password, email)
    interact_db(query=query, query_type='commit')
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', employees=employees_list, name=name, message="employee updated!")

@assignment_4.route('/assignment_4/updateEmp2', methods=['GET', 'POST'])
def update_emp2():
    email = request.form['email']
    name = request.form['name']
    print(email)
    return render_template('updateEmployee.html', email=email, name=name)

@assignment_4.route('/assignment_4/deleteEmp', methods=['GET', 'POST'])
def delete_emp():
    emp_email = request.form['email']
    query = "DELETE FROM employees WHERE email='%s';" % emp_email
    interact_db(query, query_type='commit')
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', employees=employees_list, message="employee deleted!")

@assignment_4.route('/assignment_4/employees', methods=['GET'])
def get_emps():
    query = 'select * from employees'
    employees_list = interact_db(query, query_type='fetch')
    employees_array = []
    for emp in employees_list:
        employees_array.append({
            'name': emp.name,
            'email': emp.email,
            'nickname': emp.nickname
        })
    return jsonify(employees_array)
