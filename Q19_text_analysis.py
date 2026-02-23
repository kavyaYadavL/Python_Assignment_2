def count_words(text):
    return len(text.split())
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count
def reverse_text(text):
    return text[::-1]
def is_palindrome(text):
    t = text.replace(" ", "").lower()
    return t == t[::-1]
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
def longest_word(text):
    words = text.split()
    long = ""
    for w in words:
        if len(w) > len(long):
            long = w
    return long
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    lw = longest_word(text)
    print("Longest word:", lw, f"({len(lw)} letters)")
    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    for k, v in freq.items():
        print(f"{k}: {v}", end="  ")
text = input("Enter text: ")
analyze_text(text)
