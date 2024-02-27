'''  ********* Python multiprocessing *********

multi-processing = running  task in parallel on diffrents cpu cores, bypasses GIL used for threading
                   multiprocessing = better for cpu bond task (heavy cpu usage)
                   multithreading = better for ip bond task (waiting around)

'''

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print("cpu count: ", cpu_count() )
    start_time = time.perf_counter()
    print("start at: ",start_time)

    #  counting 1 billion time
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()

    # process synchronization
    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()
    print("end at: ", end_time, "seconds")

    elapsed_time = end_time - start_time
    print(f"The code took {elapsed_time} seconds to complete.")

if __name__ == '__main__':
    main()