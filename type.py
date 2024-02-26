# duck typing = concepet where the classes of an object is less imp than the methods/attributes that 
#               that class type is not checked if minimum methods/atributes are present 
#               "if it is walks like a duck, and it quacks like a duck, then it must be a duck"'

class Duck:

    def walk(self):
        print("this duck is walking")
    
    def talk(self):
        print("this duck is quwaking")


class Chicken:

    def walk(self):
        print("this chicken is walking")
    
    def talk(self):
        print("this chicken is clucking")

class Person():
    def check(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()

person = Person()
person.check(chicken) # check accepet duck type argument but we passing chicken, 
# it will not given any error as the both chicken and duck have same artributes and methods it will not check its class type and it'll give you the result associated with the pass type object