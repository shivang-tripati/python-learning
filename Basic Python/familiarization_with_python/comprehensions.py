#  list comprehension = a way to created a new list with less syntax can mimic certain lambda function, eaiser to read
# list  = [expression for item in iterable]
#  list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable if conditional]

squares = []
for i in range(1, 11):
    squares.append(i*i)
# print(squares)
    
sqaures = [i*i for i in range(1, 11)]
print(sqaures)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
# passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "Failed" for i in students ]

# print(passed_students)

# dictionary comprehession
# dictionary  = {key : expresion for (key, value) in iterable }
# dictionary  = {key : expresion for (key, value) in iterable if condition }
# dictionary  = {key : ( expresion if/else expression)  for (key, value) in iterable }
# dictionary  = {key : function(value)  for (key, value) in iterable }




