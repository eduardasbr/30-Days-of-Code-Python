import os
os.system("cls")

# DIA 11
# Peça a idade do usuário e diga se ele é maior ou menor de idade.

print("""===== Are you allowed to enter the pub? =====
""")

age = int(input("How old are you? "))

if age >= 18:
    print("You’re good to go! Have some fun!")
else:
    print("Come on, kid... Go play some Fortnite! And don't forget to do your homework.")

