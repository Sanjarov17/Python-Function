def is_strong_password(password: str) -> bool:
    return len(password) > 8

parol = input("Parolingizni kiriting: ")

if is_strong_password(parol):
    print(" Kuchli parol!")
else:
    print("Parol kuchsiz. Uzunligini oshiring.")
