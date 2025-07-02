def ask_question(question: str, correct_answer: str):
    user_answer = input(question + "Javobingiz: ")
    if check_answer(user_answer, correct_answer):
        print(" Togri javob!")
    else:
        print(f" Notogri javob! Togri javob: {correct_answer}")

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

# === Mini Quiz Game ===
ask_question("1. Ozbekiston poytaxti qaysi shahar?", "Toshkent")
ask_question("2. 5 + 7 nechiga teng?", "12")
