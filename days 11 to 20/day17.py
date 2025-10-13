import os
os.system("cls")

# DIA 17
# Peça o ano de nascimento e diga se o usuário pode votar.

print("""
========= Can you vote? =========
""")

age = int(input("How old are you? "))

if age < 16:
    print("Can't vote!")
elif age >= 16 and age < 18:  
    print("Can vote! But it's optional.")
elif age >= 70:
    print("Can vote! But it's optional.")
else:
    print("You HAVE to vote. Mandatory.")  