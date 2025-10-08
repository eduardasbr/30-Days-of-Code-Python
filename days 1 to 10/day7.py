import os
os.system("cls")

# DIA 7
# Peça o preço de um produto e mostre o novo preço com 10% de desconto.

produtoSemDesc = float(input("Informe o preço do produto: "))

produtoComDesc = produtoSemDesc - (produtoSemDesc * 0.1)

print(f"O valor do produto com 10% de desconto é: R$ {produtoComDesc:2.2f}.")
