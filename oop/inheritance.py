class Organism:
    alive = True
     
class Animal(Organism):
    
    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

class Rabbit(Animal): #in order to inhrit pass the parent class to child(sub) class
    def run(self):
        print("This rabbit is running, now")

    # method overriding , an oblect will use mwthod that is more closely associated with itself first beofre relying on a method that amy inherit form parent class
    def eat(self,):
        print("This rabbit is eating a carrot, <- Method Overriding")


class Fish(Animal): #in order to inhrit pass the parent class to child(sub) class
    def swim(self):
        print("This fish is swimming, now")

      # method overriding    
    def eat(self,):
        print("This fish is eating a small fish <- Method Overriding")

class Hawk(Animal): #in order to inhrit pass the parent class to child(sub) class
    def fly(self):
        print("This hawk is flying , now")


# Multilevel inheritence = when a derived (child) class inherits another derived(child) class
        
# multiple inhritence 

class Prey:

    def flee(slef):
        print("This animal fless")    

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit2(Prey):
    print()  

class Hawk2(Predator):
    print()            

class Fish2(Prey, Predator):
    print()  