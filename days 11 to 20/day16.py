import os
os.system("cls")

# DIA 16
# Peça a altura e o peso, e calcule o IMC com classificação (abaixo do peso, normal, sobrepeso...).

print("""
========== BMI (Body Mass Index) CALCULATOR =========
""")

height = float(input("Type your height: "))
bodyWeight = float(input("Type your body weight:  "))


bmi = bodyWeight / height**2

if bmi < 18.5:
    print(f"Your BMI is {bmi:.1f}, Underweight")
elif bmi < 24.9:
    print(f"Your BMI is {bmi:.1f}, Normal weight")
elif bmi < 29.9:
    print(f"Your BMI is {bmi:.1f}, Overweight")
elif bmi < 34.9:
    print(f"Your BMI is {bmi:.1f}, Obesity class I")
elif bmi < 39.9:
    print(f"Your BMI is {bmi:.1f}, Obesity class II")
else:
    print(f"Your BMI is {bmi:.1f}, Obesity class III (severe)")

