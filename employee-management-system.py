# mysql connectivity 
import mysql.connector

# database connectivity steps
con = mysql.connector.connect(host="localhost", user="root", password="", database="pythondb")

# add employee function
def addEmployee():
    id = input("Enter employee id : ")
    name = input("Enter employee name : ")
    job = input("Enter employee job : ")
    sal = input("Enter employee salary : ")
    data = (id, name, job, sal)

    query = "insert into emp values(%s, %s, %s, %s)"
    c = con.cursor() 
    c.execute(query, data)
    con.commit()

    print("Employee added successfully...")
    menu()

# updateEmployee function
def updateEmployee():
    c = con.cursor()

    query = "update emp set name = %s, job = %s, sal = %s where id = %s"

    id = input("Enter the id of the employee whose information to update : ")
    newName = input("Enter new name value : ")
    newJob = input("Enter new job value : ")
    newSal = input("Enter new salary value : ")

    c.execute(query, (newName, newJob, newSal, id))

    con.commit()
    print("Employee updated successfully...")
    menu()

# remove employee 
def removeEmployee():
    c = con.cursor()

    id = input("Enter the id of the employee to remove : ")
    query = "delete from emp where id = %s"
    c.execute(query, (id,))

    con.commit()
    print("Employee deleted successfully...")
    menu()
    
# display all employees
def displayEmployee():
    c = con.cursor()

    query = "select * from emp"
    c.execute(query)
    result = c.fetchall()

    for record in result:
        print("Employee id : ", record[0])
        print("Employee name : ", record[1])
        print("Employee job : ", record[2])
        print("Employee salary : ", record[3])
    
    menu()
    
# menu function to display employee menu
def menu():
    print("Welcome to Employee Management System")
    print("Choose from the options below : ")
    print("1. Add Employee ")       # insert
    print("2. Remove Employee ")    # delete
    print("3. Update Employee ")    # update
    print("4. Display All Employees ")  # select
    print("5. Exit ")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        addEmployee()
    elif choice == 2:
        removeEmployee()
    elif choice == 3:
        updateEmployee()
    elif choice == 4:
        displayEmployee()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid choice...!")
        menu()

menu()