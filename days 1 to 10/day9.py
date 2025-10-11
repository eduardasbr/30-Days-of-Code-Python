import os
os.system("cls")

# DIA 9
# Peça a quantidade de reais e converta para dólares (1 dólar = 5,60).

print("""======= Conversor de moedas: Real para Dólar ======
      """)

real = float(input("Insira o valor em real(R$): R$"))

dolar = real * 5.60

print(f"O valor de R${real:0.2f} em dólares é: ${dolar:0.2f}")