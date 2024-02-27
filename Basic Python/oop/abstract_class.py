# Prevent use =r from creating an object of that class
#  comples a user to overrider abstract methods in a child class

#  abstract class = a class which contains one or more abtract methods. -> atleast one abstract method must be in the abstract class
#  abstract method = a method that has a declaration but does not have an implementation

 # all childern classes of abstract class must implement abstract method of its parent abstract class, otherwise you'll get error

from abc import ABC, abstractclassmethod # abc -> abstract

class Vehical(ABC):

    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass



class Car(Vehical):
    def go(self):
        print("You Drive the car")
    
    def stop(self):
        print("you stopped the car")


class Motorcycle(Vehical):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("you stopped the motorcycle")

    # pass 

# vehical = Vehical()     #Can't instantiate abstract class Vehical with abstract method 
car = Car()
motorcycle = Motorcycle()

# vehical.go()
car.go()
motorcycle.go()

