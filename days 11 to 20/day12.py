import os
os.system("cls")

# DIA 12
# Peça uma nota e diga se o aluno foi aprovado (≥ 6).

print(""" 
========= SCHOOL GRADES SYSTEM =========

""")

grade = float(input("Student's grade: "))

if grade >= 6:
    print("Passed!")
else:
    print("Failed!")

