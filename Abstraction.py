#what is abstraction 
#Abstraction is the process of hiding the implementation details of a class and showing only the essential features of the object.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
car = Vehicle()
car.start()
car.stop()