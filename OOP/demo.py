from fraction import Fraction 

def display_menu():
    print("""\nWhich Operation you want to perform:
                            1. Addition
                            2. Subtraction
                            3. Multiplication
                            4. Division
                            5. Exit""")

def get_user_choice():
    while True:
        choice = input("Please choose an option: ")
        if choice in ['1', '2', '3', '4','5']:
            return choice
        else:
            print("Invalid choice. Please try again.")


def main():

    print("Enter Numerator and Denominator Values of First Fraction:")
    num1 = int(input("Enter Numerator Value: "))
    den1 = int(input("Enter Denominator Value: "))

    print("Enter Numerator and Denominator Values of Second Fraction:")
    num2 = int(input("Enter Numerator Value: "))
    den2 = int(input("Enter Denominator Value: "))

    x = Fraction(num1,den1)
    y = Fraction(num2,den2)
    

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            print("Addition is: ",x + y)
        elif choice == '2':
            print("Subtraction is: ",x - y)
        elif choice == '3':
            print("Multiplication is: ",x * y)
        elif choice == '4':
            print("Division is:",x / y)
        elif choice == '5':
            print("Bye!")
            break


if __name__ == "__main__":
    main()
