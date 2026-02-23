def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def calculator():
    while True:
        print("\n1.Add  2.Subtract  3.Multiply")
        print("4.Divide  5.Modulus  6.Power  7.Exit")
        choice = input("Enter choice: ")
        if choice == "7":
            print("Exiting...")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid input")
            continue
        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", modulus(num1, num2))
        elif choice == "6":
            print("Result:", power(num1, num2))
        else:
            print("Invalid choice")
calculator()
