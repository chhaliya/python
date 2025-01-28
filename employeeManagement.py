# Employee Management System

# Initial employee data
employees = [
    {"employee_id": 101, "name": "tk", "salary": 300000, "city": "Delhi"},
    {"employee_id": 102, "name": "pk", "salary": 250000, "city": "Mumbai"},
    {"employee_id": 103, "name": "sk", "salary": 400000, "city": "Pune"},
]

# Function to display the menu
def display_menu():
    print("\n Employee Management System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Edit Employee")
    print("5. Delete Employee")
    print("6. Exit")

# Function to add a new employee

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    city = input("Enter City: ")
    employees.append({"employee_id": emp_id, "name": name, "salary": salary, "city": city})
    print("Employee added successfully!")

# Function to view all employees

def view_employees():
    print("\nList of Employees:")
    if employees:
        for emp in employees:
            print(f"ID: {emp['employee_id']}, Name: {emp['name']}, Salary: {emp['salary']}, City: {emp['city']}")
    else:
        print("No employees found!")

# Function to search for employees by name or city

def search_employee():
    key = input("Search by Name or City: ").lower()
    results = [emp for emp in employees if key in emp['name'].lower() or key in emp['city'].lower()]
    if results:
        for emp in results:
            print(f"ID: {emp['employee_id']}, Name: {emp['name']}, Salary: {emp['salary']}, City: {emp['city']}")
    else:
        print("No employees found!")

# Function to edit employee details

def edit_employee():
    emp_id = int(input("Enter Employee ID to edit: "))
    for emp in employees:
        if emp['employee_id'] == emp_id:
            emp['salary'] = float(input("Enter new Salary: "))
            emp['city'] = input("Enter new City: ")
            print("Employee details updated!")
            return
    print("Employee not found!")

# Function to delete an employee

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    for i, emp in enumerate(employees):
        if emp['employee_id'] == emp_id:
            employees.pop(i)
            print("Employee deleted successfully!")
            return
    print("Invalid Employee ID. Please enter a valid ID.")


while True:
    display_menu()
    num = input("Enter your choice: ")
    if num == "1":
        add_employee()
    elif num == "2":
        view_employees()
    elif num == "3":
        search_employee()
    elif num == "4":
        edit_employee()
    elif num == "5":
        delete_employee()
    elif num == "6":
        print("Exiting gn!")
        break
    else:
        print("Invalid input try again.")