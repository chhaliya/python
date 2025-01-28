from functools import reduce

class Employee:
    def __init__(self, id, name, salary, city):
        self._id = id
        self._name = name
        self._salary = salary
        self._city = city

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def set_city(self, new_city):
        self._city = new_city

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Salary: {self._salary}, City: {self._city}"


class Manager(Employee):
    def __init__(self, id, name, salary, city, department):
        super().__init__(id, name, salary, city)
        self._department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self._department}"


class ManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)
        print("Employee added successfully!")

    def view_employees(self):
        for emp in self.employees:
            print(emp)

    def search_employee(self, key):
        results = [emp for emp in self.employees if key.lower() in emp._name.lower() or key.lower() in emp._city.lower()]

        if results:
            for emp in results:
                print(emp)  
            print("Employee found successfully!")
        else:
            print("No employees found!")


    def edit_employee(self, emp_id, new_salary=None, new_city=None):
        for emp in self.employees:
            if emp._id == emp_id:
                if new_salary: emp.set_salary(new_salary)
                if new_city: emp.set_city(new_city)
                print("Employee details updated!")
                return
        print("Employee not found!")

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp._id != emp_id]
        print("Employee deleted successfully!")

    def display_names_uppercase(self):
        print("Names:", list(map(lambda emp: emp._name.upper(), self.employees)))

    def filter_high_salary(self, threshold):
        print("Filter by salary")
        for emp in filter(lambda emp: emp.get_salary() > threshold, self.employees):
            print(emp)
        

    def total_salary_expenditure(self):
        print(f"Total Salary: {reduce(lambda acc, emp: acc + emp.get_salary(), self.employees, 0)}")


if __name__ == "__main__":
    system = ManagementSystem()
    system.add_employee(Employee(1, "Tushar", 300000, "Delhi"))
    system.add_employee(Employee(2, "Pankaj", 250000, "Mumbai"))
    system.add_employee(Employee(3, "Sumit", 400000, "Pune"))
    system.add_employee(Manager(4, "TK", 500000, "Bangalore", "IT"))

    system.view_employees()
    system.search_employee("Delhi")
    system.edit_employee(2, new_salary=270000, new_city="Hyderabad")
    system.delete_employee(3)
    system.display_names_uppercase()
    system.filter_high_salary(260000)
    system.total_salary_expenditure()