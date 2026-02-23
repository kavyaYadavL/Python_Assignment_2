try:
    text = input("Enter word/number: ")
    original = text
    reversed_text = text[::-1]
    print("Original:", original)
    print("Reversed:", reversed_text)
    if original.lower() == reversed_text.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT A PALINDROME")
except:
    print("Invalid input")
