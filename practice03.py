def is_even(number):
    return number %2 ==0 


def print_even_massage(number):
    print(f"{number}Juft son")

def print_odd_message(number):
    print(f"{number}Toq son")


son = 9 
if is_even(son):
    print_even_massage(son)

else:
    print_odd_message(son)    