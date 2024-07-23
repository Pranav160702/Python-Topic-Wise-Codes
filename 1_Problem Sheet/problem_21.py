# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

def cm_to_ft():
    cm = float(input("Enter length in centimeters: "))
    ft = cm / 30.48
    print(f"{cm} centimeters is equal to {ft} feet.")


def kl_to_miles():
    kl = float(input("Enter distance in kilometers: "))
    miles = kl / 1.60934
    print(f"{kl} kilometers is equal to {miles} miles.")


def usd_to_inr():
    usd = float(input("Enter amount in USD: "))
    inr = usd * 74.83  # Assuming 1 USD = 74.83 INR
    print(f"{usd} USD is equal to {inr} INR.")


def main():
    while True:
        print("\nMenu:")
        print("1. Convert centimeters to feet")
        print("2. Convert kilometers to miles")
        print("3. Convert USD to INR")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            cm_to_ft()
        elif choice == 2:
            kl_to_miles()
        elif choice == 3:
            usd_to_inr()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
