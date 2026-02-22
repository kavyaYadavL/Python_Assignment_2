try:
    num = int(input("Enter a number: "))
    if num <= 1:
        print(num, "is NOT a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is NOT a prime number")
                break
        else:
            print(num, "is a PRIME number")
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    print("Prime numbers:", end=" ")
    for n in range(start, end + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n, end=" ")
except:
    print("Invalid input")
