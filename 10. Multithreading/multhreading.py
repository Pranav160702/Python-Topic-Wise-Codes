import threading
import time
def print_numbers(num,seconds):
    for i in range(num):
        print(f"Number: {i}")
        time.sleep(seconds)
# Create a thread using 'target'
thread = threading.Thread(target=print_numbers, args=(5,1))
# Start the thread
thread.start()
# Wait for the thread to complete
thread.join()
print("Thread has finished execution.")


# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# # Create a thread using 'target'
# thread = threading.Thread(target=print_numbers)

# # Start the thread
# thread.start()

# # Wait for the thread to complete
# thread.join()

# print("Thread has Fininshed Execution.")
