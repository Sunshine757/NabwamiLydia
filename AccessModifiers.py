#access modifiers
'''
python suports three acessmodifiers 
-public accessible everywhere
-protecetd accessible in the class and subclass
-private accessible only inside the class
'''
#example
#employee example, name, salary, age
#public
class Employee:
    def __init__(self):
        self.name = "Peter"

        emp = Employee()
        print(emp.name)

#protected we use a single underscore
class Employee:
    def __init__(self):
        self._salary = 120000000

        emp = Employee()
        print(emp._salary)

#private we use a double underscore 
class Employee:
    def __init__(self):
        self.__salary = 120000000

        emp = Employee()
        print(emp.__salary)      

        