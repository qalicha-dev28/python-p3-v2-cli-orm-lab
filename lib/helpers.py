# lib/helpers.py

from models import Department, Employee

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        if employee:
            print(employee)
        else:
            print(f"Employee {id_} not found")
    except ValueError:
        print("Please enter a valid integer for the employee id")

def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")
    except Exception as e:
        print(f"Error creating employee: {e}")

def update_employee():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        
        if not employee:
            print(f"Employee {id_} not found")
            return
        
        name = input("Enter the employee's new name: ")
        job_title = input("Enter the employee's new job title: ")
        department_id = int(input("Enter the employee's new department id: "))
        
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        
        employee.update()
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error updating employee: {e}")
    except Exception as e:
        print(f"Error updating employee: {e}")

def delete_employee():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        
        if not employee:
            print(f"Employee {id_} not found")
            return
        
        employee.delete()
        print(f"Employee {id_} deleted")
    except ValueError:
        print("Please enter a valid integer for the employee id")
    except Exception as e:
        print(f"Error deleting employee: {e}")

def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        department = Department.find_by_id(department_id)
        
        if not department:
            print(f"Department {department_id} not found")
            return
        
        employees = department.employees()
        for employee in employees:
            print(employee)
    except ValueError:
        print("Please enter a valid integer for the department id")