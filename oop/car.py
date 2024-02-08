class Car:
    make = None
    model = None
    year = None
    color = None
    wheels = 4 #class vaariable        
    def __init__(self,make, model, year, color):   # constructor, always pass self in it
        self.make = make
        self.color = color # instance variable
        self.model = model
        self.year = year

    def turn_On(self):
        print("You start the engine")
        return self # **In order to implement method chaining you'll have to return self, otherwise method chaning will not 

    def drive(self): # self -> refers to boject that is using this method
        print("This "+ self.make + self.model + " car is driving")
        return self

    def stop(self):
        print("This "+ self.make + self.model + " car is stoped")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

# ** Method chaning **
# In order to implement method chaining you'll have to return self in the method, 
# otherwise method chaning will not work, it'll give you error   
car = Car("tesla", "-EV", "2011"," red") 
car.turn_On().drive().stop().turn_off()  # method chaning -> only work when each method return self

# in a better or readable way to implement method chaining
#  (backshales) \ -> here a line continution character
car.turn_On()\
    .drive()\
    .stop()\
    .turn_off() 
