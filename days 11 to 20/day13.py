import os
os.system("cls")

# DIA 13
# Peça um número e diga se ele é positivo, negativo ou zero.

print("""
======= POSITIVE, NEGATIVE OR ZERO? =======
""")

num = float(input("Type a number: "))

if num < 0:
    print(f"The number {num} is NEGATIVE.")
elif num > 0:
    print(f"The number {num} is POSITIVE.")
else:
    print(f"The number {num} is ZERO.")

