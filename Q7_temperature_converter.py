print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = int(input("Enter your choice: "))
if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)
elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius:", c)
elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print("Kelvin:", k)
else:
    print("Invalid choice")
