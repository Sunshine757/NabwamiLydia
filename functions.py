#functions we use def function_name():
#syntax of a function
#def function_name(parameters):
#   function body
#   return value

#built in functions 
print("Hello, World!")
len("Hello, World!") #returns the length of a string
max([1, 2, 3, 4, 5]) #returns the largest item in an iterable
min([1, 2, 3, 4, 5]) #returns the smallest item in an iterable
sum([1, 2, 3, 4, 5]) #returns the sum of all items in an iterable
#the code inside a function must be idented to show that it belongs inside the function

def greet():
    print("Welcome to python programming!")

#calling a function
greet()

#parameters and arguments
def greet(name): #name is a parameter
    print(f"welcome {name} to python programming")

#calling the function with an argument
greet("Alice") #Alice is an argument
greet("Bob") #arguments are actual values passed to the function
greet("Charlie")

#keyword arguments
def greet(name, age):
    print(f"welcome {name} to python programming. You are {age} years old.")

#calling the function with keyword arguments
greet(name="Alice", age=25)
greet(age=30, name="Bob")

#default parameters 
def greet(name, age=18): #age has a default value of 18
    print(f"welcome {name} to python programming. You are {age} years old.")

#lamda functions
#lambda functions are anonymous functions that can take any number of arguments but can only have one expression
square = lambda x: x ** 2
print(square(5))  # prints 25
