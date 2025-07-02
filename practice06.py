def is_valid_phone_number(phone):
    return len("phone:" ) == 9
phone = input("phone: ")
if is_valid_phone_number(phone):
    print("valid number")

else:
    print("xato number")