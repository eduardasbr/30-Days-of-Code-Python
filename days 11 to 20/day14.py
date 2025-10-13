import os
os.system("cls")

# DIA 14
# Peça um número e diga se é par ou ímpar.

print("""
========= ODD OR EVEN? =========
""")

num = int(input("Type a number: "))

if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")
