# =================================================================
# EJERCICIO 1: Calculadora de IMC con Categorías
# Este programa calcula el IMC y muestra en qué categoría se encuentra
# =================================================================

# Pedimos los datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calculamos el IMC: peso divido por altura al cuadrado
imc =peso / (altura ** 2)

# Redondeamos
imc = round(imc, 2)

# Imprimimos resultado
print(f"Tu IMC es: {imc}")

# Estructura condicional para determinar la categoría de IMC
if imc < 18.5:
  print("Categoría: Bajo peso")
elif imc < 25:
  print("Categoría: Peso normal")
elif imc < 30:
  print("Categoría: Sobrepeso")
else:
  print("Categoría: Obesidad")