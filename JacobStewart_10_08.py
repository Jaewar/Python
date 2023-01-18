# Jacob L Stewart
# Chapter 10 Assignment 08
# Implement a superclass Person. Make two classes, Student and Instructor, that inherit from Person.
# A person has a name and a year of birth. A student has a major, and an instructor has a salary.
# Write the class declarations, the constructors, and the __repr__ method for all classes.
# Create a test program that tests these classes and methods.

# Super class @params name and year of birth
class Person:
    def __init__(self, name, year_of_birth):
        # assign variables
        self._name = name
        self._YoB = year_of_birth

    # repr to return object as string
    def __repr__(self):
        return "Person Info:\n" + "Name: " + self._name + "\nYear of birth: " + self._YoB


# subclass student inherits Person new param @major
class Student(Person):
    def __init__(self, name, year_of_birth, major):
        # @super() to use constructor from Person
        super().__init__(name, year_of_birth)
        self._major = major

    def __repr__(self):
        # repr to return object as string
        return "Student Info: \n" + "Name: " + self._name + "\n" + "Year of birth: " + self._YoB + \
               "\nMajor: " + self._major


# subclass Instructor inherits Person new param @salary
class Instructor(Person):
    def __init__(self, name, year_of_birth, salary):
        # @super() to use constructor from Person
        super().__init__(name, year_of_birth)
        self._salary = salary

    def __repr__(self):
        # repr to return object as string
        return "Instructor Info:\nName: " + self._name + "\nYear of birth: " + self._YoB + "\nSalary: " + self._salary


def main():
    # creating objects of each class
    newPerson = Person("John", "1999")
    newStudent = Student("James", "1998", "AS")
    newInstructor = Instructor("Joe", "1997", "70000")
    # display objects as strings (printing object returns repr, repr(class) also works).
    print(newPerson)
    print("--------------------")
    print(newStudent)
    print("--------------------")
    print(newInstructor)


main()
