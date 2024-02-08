# str.format() = potional metjod that give user more controal when displaying output

animal = "cow"
item = "moon"

# print("the "+animal+ " jumped over the " + item)
# print("the {} jumped over the {}".format("cow", "moon"))
# print("the {} jumped over the {}".format(animal, item))
#pclearrint("the {1} jumped over the {0}".format(animal, item)) # positioonal argument
#print("the {animal} jumped over the {item}".format(animal="goat", item="mars")) # keyword argument 

# text = "the {} jumped over the {}"
# print(text.format(animal, item))

# name = "Bro"
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}".format(name)) # center
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) #left padding
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) #right padding



# **Number**
number = 1000

print("The number is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number))# ocatal
print("The number is {:x}".format(number)) # hexadecimal
print("The number is {:X}".format(number))
