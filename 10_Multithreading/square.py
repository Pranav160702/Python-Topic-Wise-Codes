import threading
import time

def area_of_square(side):
    area = side * side
    time.sleep(1)
    print("Area of square is: ", area)


def perimeter_of_square(side):
    perimeter = 4 * side
    time.sleep(1)
    print("Perimeter of square is: ", perimeter)

def len_of_diagonal(side):
    diagonal = (side * side) ** 0.5
    time.sleep(1)
    print("Length of diagonal is: ", diagonal)


side_of_square = float(input("Enter the Side of the Square: "))
start_time = time.time()
t1 = threading.Thread(target=area_of_square, args=(side_of_square,))
t2 = threading.Thread(target=perimeter_of_square, args=(side_of_square,))
t3 = threading.Thread(target=len_of_diagonal, args=(side_of_square,))
t1.start()
t2.start()  
t3.start()
t1.join()
t2.join()
t3.join()

# area_of_square(side_of_square)
# perimeter_of_square(side_of_square)
# len_of_diagonal(side_of_square)

end_time = time.time()
print("Time taken to execute the program is: ", end_time - start_time)
