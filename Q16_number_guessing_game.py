import random
best = None
while True:
    num = random.randint(1, 100)
    attempts = 7
    used = 0
    while attempts > 0:
        try:
            guess = int(input("Guess (1-100):"))
            used += 1
            attempts -= 1
            if guess == num:
                print("Correct!Attempts used:",used)
                if best is None or used < best:
                    best = used
                break
            elif guess > num:
                print("Too high!", attempts,"left")
            else:
                print("Too low!", attempts,"left")
            if abs(guess - num) <= 5 and guess!= num:
                print("Close!")
        except:
            print("Invalid input")
    else:
        print("Game over! Number was:", num)
    if input("Play again? (yes/no):").lower()!= "yes":
        print("Best score:",best)
        break
