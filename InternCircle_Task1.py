def arithmetic():
    print("\n--- Arithmetic Operations ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def unit_conversion():
    print("\n--- Unit Conversion ---")
    print("1. Km to Miles")
    print("2. Miles to Km")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    choice = input("Choose option: ")

    try:
        if choice == '1':
            km = float(input("Enter kilometers: "))
            print("Miles:", km * 0.621371)
        elif choice == '2':
            miles = float(input("Enter miles: "))
            print("Kilometers:", miles / 0.621371)
        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", (c * 9/5) + 32)
        elif choice == '4':
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", (f - 32) * 5/9)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def currency_conversion():
    print("\n--- Currency Conversion ---")
    print("1. INR to USD")
    print("2. USD to INR")
    choice = input("Choose option: ")

    try:
        if choice == '1':
            inr = float(input("Enter INR: "))
            print("USD:", inr * 0.012)  # Example rate
        elif choice == '2':
            usd = float(input("Enter USD: "))
            print("INR:", usd * 83.0)   # Example rate
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def main():
    while True:
        print("\n=== Interactive Calculator & Converter ===")
        print("1. Arithmetic")
        print("2. Unit Conversion")
        print("3. Currency Conversion")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            arithmetic()
        elif choice == '2':
            unit_conversion()
        elif choice == '3':
            currency_conversion()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
