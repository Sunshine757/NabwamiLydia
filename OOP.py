#python classes
class Person:
    def __init__(self, name, age): #constructor method
        #intializing the attrubutes of the class
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

        #creating an instanceof a class
        person1 = Person("Alice", 30)
        person1.greet()
        print(person1.name)