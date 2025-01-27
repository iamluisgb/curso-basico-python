### Ejercicio 1: Calculadora de Impuestos 💰

**Enunciado:**
Crea un programa que calcule el impuesto a pagar según el salario anual introducido.
Los rangos de impuestos son:
- Hasta $10,000: 5% de impuesto
- De $10,001 a $20,000: 10% de impuesto
- De $20,001 a $35,000: 15% de impuesto
- De $35,001 a $60,000: 20% de impuesto
- Más de $60,000: 30% de impuesto

El programa debe mostrar:
1. El salario bruto
2. El porcentaje de impuesto aplicado
3. El monto de impuesto a pagar
4. El salario neto final

```python
# Solución: Calculadora de Impuestos

# Pedimos el salario anual
salario_anual = float(input("Ingresa tu salario anual: $"))

# Inicializamos el porcentaje de impuesto
porcentaje_impuesto = 0

# Determinamos el porcentaje según el rango
if salario_anual <= 10000:
    porcentaje_impuesto = 5
elif salario_anual <= 20000:
    porcentaje_impuesto = 10
elif salario_anual <= 35000:
    porcentaje_impuesto = 15
elif salario_anual <= 60000:
    porcentaje_impuesto = 20
else:
    porcentaje_impuesto = 30

# Calculamos el impuesto y el salario neto
impuesto = salario_anual * (porcentaje_impuesto / 100)
salario_neto = salario_anual - impuesto

# Mostramos los resultados
print("\n=== Resumen de Impuestos ===")
print(f"Salario Bruto: ${salario_anual}")
print(f"Porcentaje de Impuesto: {porcentaje_impuesto}%")
print(f"Impuesto a Pagar: ${impuesto}")
print(f"Salario Neto: ${salario_neto}")
```

### Ejercicio 2: Piedra, Papel o Tijera ✌️

**Enunciado:**
Crea un juego de Piedra, Papel o Tijera donde el usuario juegue contra la computadora.
- La computadora debe elegir aleatoriamente
- El programa debe mostrar quién ganó y por qué
- Debe validar que el usuario ingrese una opción válida

```python
# Solución: Piedra, Papel o Tijera
import random

# Mostramos las opciones al usuario
print("Juguemos a Piedra, Papel o Tijera!")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

# Obtenemos la elección del usuario
eleccion_usuario = input("Elige tu opción (1-3): ")

# Validamos la entrada del usuario
if eleccion_usuario == "1" or eleccion_usuario == "2" or eleccion_usuario == "3":
    # Convertimos la elección a número
    eleccion_usuario = int(eleccion_usuario)

    # Generamos la elección de la computadora (1, 2 o 3)
    eleccion_computadora = random.randint(1, 3)

    # Mostramos la elección del usuario
    if eleccion_usuario == 1:
        print("\nTú elegiste: Piedra")
    elif eleccion_usuario == 2:
        print("\nTú elegiste: Papel")
    else:
        print("\nTú elegiste: Tijera")

    # Mostramos la elección de la computadora
    if eleccion_computadora == 1:
        print("La computadora eligió: Piedra")
    elif eleccion_computadora == 2:
        print("La computadora eligió: Papel")
    else:
        print("La computadora eligió: Tijera")

    # Determinamos el ganador
    if eleccion_usuario == eleccion_computadora:
        print("\n¡Empate!")
    elif eleccion_usuario == 1 and eleccion_computadora == 3:
        print("\n¡Ganaste! Piedra vence a Tijera")
    elif eleccion_usuario == 2 and eleccion_computadora == 1:
        print("\n¡Ganaste! Papel vence a Piedra")
    elif eleccion_usuario == 3 and eleccion_computadora == 2:
        print("\n¡Ganaste! Tijera vence a Papel")
    else:
        print("\n¡La computadora gana!")

else:
    print("¡Opción no válida! Debes elegir 1, 2 o 3")
```
