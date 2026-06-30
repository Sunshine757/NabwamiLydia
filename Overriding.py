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

#overriding
class Teacher(Person):
    def display(self):
        print("Name:", self.name)
        print("I am a teacher.")
#using the super() function to call the parent class method
    def display(self):
        super().display()
        print("I am a teacher.")
