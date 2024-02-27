# threads = a flow of execution. Like a seprate order of instruction
#                     however each threads takes a turn running to achieve concurrency
#                     GIL(Global, Interpreter lock)
#                    allows only one thread to hold the control of the python interpreter 

#  cpu bound = program/task use multiprocessing
# io bond = program/ task  use multi-threading

import threading
import time

# example :- in quiz game while we were waiting for user input(i/o bound task), we could have countdown time going(there is limit of time to ans a qus)   


def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drink coffee")

def study():
    time.sleep(5)
    print("you study")

# all these methods will be callled one by one as only one ( main) thread is executing
    # toal time to run this programe will be 3 + 4 + 5 = 12 sec
# eat_breakfast()
# drink_coffee()
# study()
    
# creating additional threads
x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=())

# total time to run the program is 5 sec as the threads are running concurrently
x.start()
y.start()
z.start()

#  here  active_count() & numerate will called before threads x, y, z finsh their respexted tasks
# this is cause main thread will not going to wait arround for these three threads to complete. 
# it has it's on set of instruction, so it is no longer incharge of the three functions eat_breakfast(), drink_coffee() & study()
#  it's job is create threads x, y, z and to print active_count() & enumerate() which finnish before threads x, y, z

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter()) # how long it takes our calling thread (main) to finsih it set of instruction



## thread Synchroniation =  the main(calling) thread wait arround for another thread to accomplish there task 
# before it can move on with its own instruction set

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
