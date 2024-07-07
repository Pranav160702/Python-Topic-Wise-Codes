import threading

balance = 200

def deposit(amount, time):
    global balance

    for _ in range(10):
        balance += amount

def withdraw(amount, time):
    global balance
    for _ in range(10):
        balance -= amount


deposite_thread = threading.Thread(target=deposit, args = [1, 10005200015110])
withdraw_thread = threading.Thread(target=withdraw, args = [1, 1002555441100000])

deposite_thread.start()
withdraw_thread.start()

deposite_thread.join()
withdraw_thread.join()

print(balance)