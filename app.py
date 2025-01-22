from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)


# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='student',
    database='employee_db'
)
cursor = db.cursor()

# Home route
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/db_all')
def db_all():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)

# Add employee
@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']
    
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", (name, department, salary))
    db.commit()
    return redirect(url_for('db_all'))

# Delete employee
@app.route('/delete/<int:id>')
def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('db_all'))
# Increment salary
@app.route('/increment/<int:id>', methods=['POST'])
def increment_salary(id):
    increment = request.form['increment']
    cursor.execute("UPDATE employees SET salary = salary + %s WHERE id = %s", (increment, id))
    db.commit()
    return redirect(url_for('db_all'))
# Show all employees
@app.route('/employees')
def all_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('employees.html', employees=employees)
@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == "POST" and request.form["username"] == "Haimabati" and request.form["password"]=='haima@2209': 
        return redirect(url_for("db_all")) 
    # if the method is GET or username is not admin, 
    # then it redirects to index method. 
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)
