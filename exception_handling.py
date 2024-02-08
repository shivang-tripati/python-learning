# exception = events detecte dduring execution that iteruupts the flow of A PROGRAME

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a no. to divided by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by Zero! idiot!")
except ValueError as e:
    print(e)
    print("enter no. only pls")
except Exception as e:
    print(e)
    print("something went wrong :( ")
else:  # if no exception occur execute this
    print(result)
finally:
    print("Finallly block ->" + " This will always execute")