# lambda function : func written in One(1) line using lambda keyword
                #    accepets any no. of keyword but has only one expression   
# lambda parameters:expression

# normal function
def double(x):
    return x*2
print(double(5))

triple = lambda x : x * 3
multiply = lambda x,y: x*y

full_name = lambda first_name, last_name : first_name + " " + last_name
age_cehck = lambda age: True if age >= 18 else False

print(age_cehck(15))
print(full_name("Bro", "Code"))
print(triple(5))
print(multiply(4, 8))