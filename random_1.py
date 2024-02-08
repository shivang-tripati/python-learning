import random

x = random.randint(1,6) # b/w 1 & 6
y = random.random() # genrate random no. b/w 0 & 1

myList =  ['rock', "paper", "scissors"]
z = random.choice(myList)

# SHUFFLE
cards = [1,2,3,4,5,6,7,8,9, "A", "B", "C", "X", "Y", "Z"]
random.shuffle(cards)
print(cards)