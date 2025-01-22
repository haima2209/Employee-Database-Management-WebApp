import mysql.connector 
con=mysql.connector.connect(host='localhost',user='root',password='student',database='student')
cursor=con.cursor(buffered=True)
#to check if an employee exists or not
def check_employee(employee_id):
    sql='SELECT * FROM EMPLOYEES WHERE ID=%s'
    cursor.execute(sql,(employee_id,))
    employee = cursor.fetchone()
    return employee is not None
def add_employee():
    Id=input('Enter Employee Id:')
    if check_employee(Id)==True:
        print('Employee already exists..Please Try Again!.')
    else:
        Name=str(input('Enter Employee Name:  '))
        Post=str(input('Enter Employee Post:  '))
        Salary=int(input('Enter Employee Salary:  '))
        sql='Insert Into EMPLOYEES values (%s,%s,%s,%s)'
        data=(Id,Name,Post,Salary)
        try:
            cursor.execute(sql,data)
            con.commit()
            print('Employee Added Successfully')
        except  mysql.connector.Error as err:
            print(f'Error:{err}')
            con.rollback()
        finally:
            cursor.close()
def remove_employee():
    Id=input('Enter Employee Id: ')
    if not check_employee(Id):
        print('Employee doesnot exist...Please try again.')
        return
    sql='DELETE FROM EMPLOYEES WHERE Id=%s'
    data=(Id,)
    try:
         cursor.execute(sql,data)
         con.commit()
         print('Employee removed successfully')
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        con.rollback()
    finally:
            cursor.close()
def promote_employee():
    Id=input('Enter Employee Id: ')
    if not check_employee(Id):
        print('Employee does not exists...Please try again!')
        return
    try:
        Amount=float(input('Enter increase in salary: '))
        sql_select='SELECT SALARY FROM EMPLOYEES WHERE id=%s'
        cursor.execute(sql_select,(Id,))
        current_salary=cursor.fetchone()[0]
        new_salary=current_salary+Amount
        sql_update='Update employees set salary=%s where id=%s'
        cursor.execute(sql_update,(new_salary,Id))
        con.commit()
        print('Employee Promoted Successfully')
    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()
    finally:
            cursor.close()
def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
            cursor.close()
            

# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()


