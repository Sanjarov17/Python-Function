def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "Kam vazn"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Ortiqcha vazn"
    else:
        return "Semizlik"

weight = float(input("Vazningizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (m): "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)

print(f"BMI: {bmi:.2f}")
print(f"Holat: {status}")
