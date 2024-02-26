#  sort() method = used with list
# sorted() dunction = used with iterables // return a new list with sorted item

# * you can use sorted with list but cannot sort with iterables

# list
students = [
            ("Amit", "F", 60),
            ("Rajan", "A", 38),
            ("Shiwam", "D", 36),
            ("Alok", "B", 20),
            ("Sandy", "C", 75)]

# grade = lambda grades : grades[1]
age = lambda ages : ages[2]
students.sort(key = age, reverse=True) #list will be sorted, tuples wsie, if you provide kry then it will sorted considering the key
# for i  in students:
#     print(i)


# tuples
student2 = (("Amit", "F", 60),
            ("Rajan", "A", 38),
            ("Shiwam", "D", 36),
            ("Alok", "B", 20),
            ("Sandy", "C", 75))

sorted_students = sorted(student2, key=age)
# for i  in sorted_students:
#     print(i)


# map() = applies a fuction to each item in iterable(list, tuple, etc)
# map(function, iterable)

store = [("shirts", 23.00),
         ("pants", 28.05),
         ("jacket", 50.00),
         ("socks", 12.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)

# filter() =  creates a collection of elements from an iterable for which a fucntion  return true
    # filter(function, 5iterable)

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            perform function on first two elemetns and repeat untill 1 value remaining
#  reduce(fuction, iterable)
