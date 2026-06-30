#what is plymorphism?
#Polymorphism is a concept in object-oriented programming that allows objects of different types to be treated as instances of the same type through a common interface. It enables a single interface to be used to represent different underlying data types or classes.
#why polymorphism
'''
-default parameters
-variables lenght arguments 
-type checking


'''
class Animal:
    def speak(self):
        return "Animal speaks"
    
#method overloading
class Dog(Animal):
    def speak(self):
        return "Dog barks" 
       
