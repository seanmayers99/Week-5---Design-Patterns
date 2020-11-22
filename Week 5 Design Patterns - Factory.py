# Sean Mayers
# 11/22/2020
# Week 5 Design Patterns - Abstract Factory Design Patterns

from abc import ABCMeta, abstractmethod

""" Abstract factory pattern you don't have individual objects and have to worry about doing instanciation that way
    Recommendation to use this pattern for time keeping for a sample of employee personal data """

class Employee(metaclass=ABCMeta):
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

        @abstractmethod
        def get_role(self):
            pass

    def __str__(self):
        return "{} - {}, {} years old {}, {} per year".format(self.__class__. __name__, self.name, self.age, self.gender, self.salary)

class Engineer(Employee):
    def get_role(self):
        return "engineering"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administration"

class EmployeeFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == 'engineer':
            return Engineer(*args)
        
        elif name == 'accountant':
            return Accountant(*args)
        
        elif name == 'admin':
            return Admin(*args)

def main():
    factory = EmployeeFactory()
    print (factory.create('engineer', 'John', 25, 'M', '$62,000'))
    print (EmployeeFactory.create('engineer', 'Samantha', 28, 'F', '$65,000')) #better

    accountant = factory.create('accountant', 'Nicole', 39, 'F', '$51,000')
    print (accountant)

    admin = factory.create('Admin', 'Susan', 32, 'F', '$45,000')
    print(admin.get_role())

main()