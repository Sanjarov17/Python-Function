def qushish(a, b):
    result = a + b
    return result

def ayirish(a, b):
    result = a - b
    return result

def kupayritish(a, b):
    result = a * b
    return result

def bulish(a, b):
    result = a / b
    return result


def main():
    a = float(input("a = "))
    b = float(input("b = "))

op = input("amal (+, -, *, /): ")


if op == '+':
    print(qushish(a, b))
elif op == '-':
    print (ayirish(a, b))
elif op == '*':
    print (kupayritish(a, b))
elif op == '/':
    print (bulish(a, b))
else:
    print(' xato amal')

main()