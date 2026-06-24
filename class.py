class Student:
    #define the attributes
    name = "Lydia"
    age  = 20
    nationality = "Ugandan"

    #using the _int_ method
    def __init__(self,name,age):
        self.name = name
        self.age = age

        #creating and object
        student1 = Student("Lydia",20)

