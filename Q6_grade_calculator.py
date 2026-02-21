m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))
m4 = int(input("Marks 4: "))
m5 = int(input("Marks 5: "))
total = m1 + m2 + m3 + m4 + m5
per = total / 5
print("Total:", total)
print("Percentage:", per)
if per >= 90:
    print("Grade: A+")
elif per >= 80:
    print("Grade: A")
elif per >= 70:
    print("Grade: B")
elif per >= 60:
    print("Grade: C")
elif per >= 50:
    print("Grade: D")
else:
    print("Grade: F")
if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
