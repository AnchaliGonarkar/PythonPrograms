def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def menu():
    print("Menu:")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.EXIT")

while True:
    menu()
    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the program.")
        break

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
            operation = "addition"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == 4:
            result = divide(num1, num2)
            operation = "division"

        print(f"The result of the {operation} is: {result}\n")
    else:
        print("Invalid choice. Please try again.\n")
