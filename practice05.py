def check_guess(secret, guess):
    return secret == guess

def print_resulst(is_correct):
    if is_correct:
        print("togri topdingiz")
    else:
        print("topolmadingiz")


def main():
    secret =45

    guess = int(input("Taxmin qiling maxfiy son: "))

    is_correct = check_guess(secret, guess )
    print_resulst(is_correct)

main()            