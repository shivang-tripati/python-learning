# zip(*iterables) = aggregate elements from two or more two iterables (list, tuple, set etc.)
# cretaes a zip object with paired elements stored in tuples for each elements 

username = ["Dude", "Bro", "Mister"]
password = ["p@ssword", "abc@123", "guest@342"]
email = ["duse@memail", "Bro@email", "huest@emnail"]

users = zip(username, password, email)
print(type(users))
for i in users:
    print(i)