# index operator [] = give access to a sequence's of elements (str, list, tuples)
name = "bro Code!"
# print(name[-1])

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:].lower()
# print(first_name)
# print(last_name)    

 # functions
# def hello(name):
#     print("hello " + name)
def add(num1, num2):
    return num1 + num2

# print(add(2, 5))
# hello("dude") 



#    nested funcation calls
# print(round(abs(float(input("Enter a whole positive number: ")))))

## Scope =>for scope python follow LEGB rule where L = Local, E = Enclosing, G = Global, B = Built-in 

## *args = parameter that will pack all argument into a tuple(tuple object does not support item assignment ) 
#           useful so that a fucntion can accepet a varying amount of arguments

def add(*args):
    sum = 0
    # to change item of the ars first you need to change it from default(tuple) to list type object
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum
# print(add(1,2,3,4,5,6,7,8,9))  

# **Kwars = parameter that will pack all arguments into a dictionary useful so that a 
#           function can accepet a varying amount of keyword argument

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello ", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Bro", middle="Dude", last="code")

# Higher Order Function = a function taht either :
                        # 1. accepets a function as an argument
                        #   or 
                        # 2. return a function
                     #  ( in python function are also trated as objects )

# First-Class Objects: In Python, functions are first-class objects12. This means that functions in Python have properties just like any other object (like strings, lists, dictionaries, etc.).
#  They can be assigned to variables, stored in data structures, passed as arguments to other functions, and even returned as values from other functions312

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# 1. a function that accepet func as argument
def hello(func):
    text = func("Hello, BRO")
    print(text)

hello(loud)
hello(quiet)

# 2.  a func that return  a function

def divisor(x):
    def divided(y):
        return y/x
    return divided

divide = divisor(2)
print(divide(10))