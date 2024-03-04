# The enumerate() function in Python is a powerful tool for working with iterators. Here’s what you need to know:

# Purpose: The primary purpose of enumerate() is to add a counter to an iterable (such as a list, tuple, or string) and return it as an enumerating object.
# Syntax: The function signature is as follows : numerate(iterable, start=0) 
#  *iterable: Any object that supports iteration.
# *start: The optional starting index for the counter (default is 0).

# Returned Object: The result of enumerate() is an enumerating object, which is an iterator that produces a sequence of tuples. 
# Each tuple contains an index (the counter) and the corresponding value from the iterable. e.g.

l1 = ["eat", "sleep", "repeat"]
obj1 = enumerate(l1)
print("Return type:", type(obj1))
print(list(enumerate(l1)))

# Output: Return type: <class 'enumerate'>  [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# Changing the starting index:

s1 = "geek"
print(list(enumerate(s1, 2)))

# Output: [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

for ele in enumerate(l1):
    print(ele)
for count, ele in enumerate(l1, 100):
    print(count, ele)

#  (0, 'eat') (1, 'sleep')  (2, 'repeat')
# 100 eat, 101 sleep, 102 repeat,

# Accessing the next element:    
fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)
next_element = next(enum_fruits)
print(f"Next Element1: {next_element}")
next_element = next(enum_fruits)
print(f"Next Element2: {next_element}")
next_element = next(enum_fruits)
print(f"Next Element3: {next_element}")


#output: Next Element: (0, 'apple')











