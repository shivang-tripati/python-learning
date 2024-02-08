#  **method overriding , an oblect will use mwthod that is more closely associated with itself
#        first beofre relying on a method that amy inherit form parent class

from car import Car
# within __init_ method we need 5 arguemtns in order to construct a car
car_1 = Car("alto", "-800", "2015"," white") # but when we pass in our object's argument, we are not passing anything for self, python done automatically
car_2 = Car("tesla", "-EV", "2011"," red")
# car_1.drive()
# car_1.stop()
# car_2.drive()
# car_2.stop()
# print(car_1.wheels)
# Car.wheels = 2 # if you make change using Class it will effect to all the objects created using the class
# print(Car.wheels)
# car_1.wheels = 2 # while if you do same using refrence variable, it will reflect changes only to object that the reference variable is pointing
# print(car_1.wheels) 
# print(car_2.wheels)

from inheritance import Animal, Rabbit, Fish, Hawk

# Animal -> Parent class
#  Fish, Rabbit, Hawk -> parent class, all they have feature of parent Animal class
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.eat()
rabbit.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()


# multiple inheritence part
from inheritance import  Rabbit2, Fish2, Hawk2
rabbit2 = Rabbit2()
fish2 = Fish2()
# hawk2 = Hawk2()  # **hwak inherit only Predator so it has acces to only haunt() method
# rabbit2.flee()   # **rabbit inherit only Prey so it has acces to only flee() method
# fish2.flee()   # **fish is inheritng both class Prey & Predator, so it has both access to both method flee() from Prey & haunt() from Predator here multiple inheritence is happing
# fish2.hunt()   #   so it has both access to both method flee() from Prey & haunt() from Predator


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.wifth = width
        

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width    

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height  

    def volume(self):
        return self.length * self.width * self.height          

square = Square(3, 3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())








