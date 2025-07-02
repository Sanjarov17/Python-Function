def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return tax

def calculate_net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax

salary = float(input("Maoshingizni kiriting: "))

tax = calculate_tax(salary)
net = calculate_net_salary(salary)

print(f"Soliq miqdori: {tax:.2f} so'm")
print(f"Toza maosh (soliqdan keyin): {net:.2f} so'm")
