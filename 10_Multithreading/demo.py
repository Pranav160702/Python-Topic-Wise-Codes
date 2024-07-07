from time import time, sleep
import threading

start_time = time()

def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up...{id}")


threads = [threading.Thread(target=something, args = []) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
# thread1 = threading.Thread(target=something,args =[0])
# thread2 = threading.Thread(target=something, args = [1])

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


# Do something
# for _ in range(10):
#     something()

end_time = time()
print(f"Main thread ended in {end_time - start_time} seconds")