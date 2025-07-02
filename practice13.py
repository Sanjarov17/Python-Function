def is_palindrome(text: str) -> bool:
    return text == text[::-1]


soz = input("So'zni kiriting: ")

if is_palindrome(soz):
    print(" Bu so'z palindrom!")
else:
    print(" Bu so'z palindrom emas.")
