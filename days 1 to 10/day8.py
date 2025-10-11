import os
os.system("cls")

# DIA 8
# Peça a temperatura em °C e converta para °F.

print("""======= Conversor de temperaturas: Celcius para Fahrenheit======
      """)

celcius = float(input("Insira a temperatura em °C: "))

fahrenheit = (celcius * 9/5) + 32

print(f"A temperatura {celcius}°C em fahrenheit é: {fahrenheit}°F")



