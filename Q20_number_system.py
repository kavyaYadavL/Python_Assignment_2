def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))
def reverse_number(n):
    return int(str(n)[::-1])
def is_armstrong(n):
    s = 0
    power = len(str(n))
    for d in str(n):
        s += int(d) ** power
    return s == n
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
def math_menu():
    while True:
        print("\n1.Factorial 2.Prime 3.Fibonacci")
        print("4.SumDigits 5.Reverse 6.Armstrong")
        print("7.GCD 8.LCM 9.Perfect 10.Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            print("Exiting...")
            break
        if choice in ["1","2","3","4","5","6","9"]:
            n = int(input("Enter number: "))
        if choice in ["7","8"]:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

        if choice == "1":
            print("Result:", factorial(n))
        elif choice == "2":
            print("Prime?" , is_prime(n))
        elif choice == "3":
            print("Fibonacci:", fibonacci(n))
        elif choice == "4":
            print("Sum of digits:", sum_of_digits(n))
        elif choice == "5":
            print("Reversed:", reverse_number(n))
        elif choice == "6":
            print("Armstrong?" , is_armstrong(n))
        elif choice == "7":
            print("GCD:", gcd(a, b))
        elif choice == "8":
            print("LCM:", lcm(a, b))
        elif choice == "9":
            print("Perfect number?", is_perfect_number(n))
        else:
            print("Invalid choice")
math_menu()
