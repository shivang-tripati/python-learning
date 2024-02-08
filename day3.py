# **list = used to store multiple items

num = [1,2,3,4,5,6,7,8,9]
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
special_char = ["1", "@", "#", "$", "%", "&", "*", "^", "~"]
 
# list2d = [num, letter, special_char]
# print(list2d[1][2])


# for x in list2d:
#     print(x)

# tuple = collection, that is ordered and unchagable used to group together related data
student = ("alok", 21, "male", "che")

# set = collection which is unordered, unidexed,  no duplicates data

utensils = {"fork", "spoon", "knife", "cup"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
dishes.update(utensils)

dinner_table = utensils.union(dishes)

# for x in dinner_table:
    # print(x)

# ** dictionary = A changable, unorderd collection of unique key:value pairs(more like object)
#    Fast cause they use hashing, allow access to value quickely 


