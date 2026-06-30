# Encapsulation in Python
#Student attributes
#age , reg number, name, course
class Student:
    def __init__(self, name, age, student_number):
        
        self.name = name
        self.age = age
        self.student_number = student_number

        student1 = Student("kylie", 20, 23456)
        print(student1.name)

                