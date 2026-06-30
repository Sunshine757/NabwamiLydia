#what is inheritance
#Inheritance is a mechanism in which one class acquires the properties and methods of another class. The class that inherits is called the subclass, and the class being inherited from is called the superclass.
'''
parent/super/base class
child/sub/derived class


'''
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

#class child
class Student(Person):
    def study(self):
        print("i ama studying python")

student1 = Student("Kylie")
student1.display()
student1.study()