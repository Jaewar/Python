# Jacob L Stewart
# Chapter 10 Assignment 09
# Make a class Employee with a name and salary. Make a class Manager inherit from Employee.
# Add an instance variable, named _department, that stores a string.
# Supply a method __repr__ that prints the manager’s name, department, and salary.
# Make a class Executive inherit from Manager.
# Supply appropriate __repr__ methods for all classes.
# Create a test program that tests these classes and methods.

# Super class @params name and salary
class Employee:
    def __init__(self, name, salary):
        # assign variables
        self._name = name
        self._salary = salary

    # repr to return object as string
    def __repr__(self):
        return "Employee: " + self._name + "," + str(self._salary)


# Super class Manager inherits Employee and adds @department
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        # assign new variable
        self._department = department

    # repr to return object as string
    def __repr__(self):
        return "Manager: " + self._name + "," + str(self._salary) + "," + self._department


# subclass Executive inherits manager
class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    # repr to return object as string
    def __repr__(self):
        return "Executive: " + self._name + "," + str(self._salary) + "," + self._department


def main():
    # creating objects of each class
    newEmployee = Employee("John", 22000)
    newManager = Manager("James", 33000, "Finance")
    newExecutive = Executive("Joe", 55000, "Finance")
    # display objects as strings (printing object returns repr, repr(class) also works).
    print(newEmployee)
    print(newManager)
    print(newExecutive)


main()
