import os
os.system("cls")

# DIA 15
# Peça duas notas e diga se o aluno foi aprovado, reprovado ou ficou de recuperação.

print(""" 
========= SCHOOL GRADES SYSTEM =========
""")


# 10 to 6 passed| 4 to 0 failed | 5 in remedial

grade = float(input("Type the student's grade: "))

if grade >= 10:
    print("Passed!")
elif grade == 5:
    print("In remedial!")
else:
    print("Failed!")
