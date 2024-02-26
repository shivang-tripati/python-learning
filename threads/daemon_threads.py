# daemon thread =  a thread that runs in the background not important for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non - daemon threads cannot ber normally killed, stay alive until task is complete
#              ex. backgorund task, garbadge collection, witing for input, long running processes
 


import threading
import time

#  example - why daemon threads can be usefull ??   
    #   there is issue with using non-daemon thread for background task such as countdown timer
#  Like. here out main thread will be in charge of waiting around for some user input & thread X is running the countdown time
#        so if you wish to exit the program, you won't be exit as long as non-daemon thread is ruuning as background task 

def timer():
    print()
    count  = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer)
        
# for daemon thread set daemon = true
# x = threading.Thread(target=timer, daemon=True)
# or
x.setDaemon(True)
x.start()


print(x.isDaemon())

amswer = input("do you wish toe exit?")
