import os
os.system("cls")

# DIA 10
# Peça dois números e mostre qual é o maior.

print("""===== Qual é o maior entre dois números? =====
""")

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")