"""
RETO: Calculadora de Área de Rectángulo 🟥
¡Vamos a crear una calculadora que nos ayude a encontrar el área de un rectángulo!

Tu programa debe:
1. Pedir al usuario la base del rectángulo
2. Pedir al usuario la altura del rectángulo
3. Calcular el área multiplicando base por altura
4. Mostrar el resultado en pantalla

Ejemplo de ejecución:
¿Cuál es la base del rectángulo? 5
¿Cuál es la altura del rectángulo? 3
El área del rectángulo es: 15
"""

# Pedimos la base del rectángulo
base = input("¿Cuál es la base del rectángulo? ")
base = float(base)

# Pedimos la altura del rectángulo
altura = input("¿Cuál es la altura del rectángulo? ")
altura = float(altura)

# Calculamos el área
area = base * altura

# Mostramos el resultado
print("El área del rectángulo es: " + str(area))