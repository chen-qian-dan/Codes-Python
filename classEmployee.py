class Employee:
    # class variable
    # it must be accessed as Employee.empCount from inside or outside the class;
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # the first argument to each method is self.
    # Python adds the self argument to the list for you,
    # you do not need to include it when you call the methods.
    def displayCount(self):
        print("Totoal Employee %d", Employee.empCount)

    def displayEmployee(se):
        print("Name : ", se.name, ", Salary: ", se.salary)

    def noSelf(name):
        print("it is okay a method without self argument?")


class Student:
    studentCount = 0

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        Student.studentCount += 1




