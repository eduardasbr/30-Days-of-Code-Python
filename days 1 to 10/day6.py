import os
os.system("cls")

# DIA 6
# Peça um número inteiro e mostre seu dobro, triplo e raiz quadrada.

num = int(input("Informe um número: "))

dobro = num * 2
triplo = num * 3
raizQ = num ** 0.5

print(f"""
Você informou o número: {num}.
      
Dobro............: {dobro}
Triplo...........: {triplo}
Raiz Quadrada....: {raizQ:.2f}
    
""")