# Write a program that will convert celsius value to fahrenheit and vice versa(Menu Driven)
# celsius = (fahrenheit - 32) * 5/9
# fahrenheit = (celsius * 9/5) + 32
# 
# ==================================================================
def display_menu():
    print("""What you want to Calculate:
          1. Celcius To Fahrenheit
          2. Fahrenheit To Celcius
          3. Exit""")
    

def get_user_choice():
    while(True):
        choice = int(input("Enter your choice: "))
        if(choice in [1,2,3]):
            return choice
        else:
            print("Invalid Choice, Please Try Again")


def cal_celcius():
    celsius = float(input("Enter the celsius value: "))
    fahrenheit = (celsius * 9/5) + 32   
    print("The fahrenheit value is: ", fahrenheit)

def cal_fahrenheit():
    fahrenheit = float(input("Enter the fahrenheit value: "))
    celsius = (fahrenheit - 32) * 5/9
    print("The celsius value is: ", celsius)


while(True):
    display_menu()
    choice = get_user_choice()
    match choice:
        case 1:
            cal_fahrenheit()
        case 2:
            cal_celcius()
        case 3:
            break


