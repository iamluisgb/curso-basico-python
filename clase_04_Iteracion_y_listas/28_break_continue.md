# Control de Bucles en Python: break y continue 🎮

## Introducción: Los Botones de Control de Nuestros Bucles

Imagina que estás viendo una serie de TV. A veces quieres saltar un episodio completo (continue) y otras veces necesitas dejar de ver por hoy (break). En programación, break y continue funcionan de manera similar: son herramientas que nos dan control sobre cómo se ejecutan nuestros bucles.

## La Instrucción break: El Botón de "Parar" 🛑

### ¿Qué es break?
break es una instrucción que nos permite salir inmediatamente de un bucle, sin importar si la condición original todavía es verdadera. Es como tener un botón de emergencia que dice "detener todo".

### Ejemplo Práctico: El Juego de la Adivinanza
```python
# Juego donde el jugador tiene que adivinar un número
numero_secreto = 7
intentos_maximos = 3
intentos_actuales = 0

print("=== ¡Adivina el Número! ===")
print("Es un número entre 1 y 10")

while intentos_actuales < intentos_maximos:
    # Mostramos los intentos restantes
    intentos_restantes = intentos_maximos - intentos_actuales
    print(f"\nTe quedan {intentos_restantes} intentos")

    # Pedimos un número
    numero = int(input("Tu número: "))

    # Si adivinó, usamos break para terminar el juego
    if numero == numero_secreto:
        print("¡Felicitaciones! ¡Adivinaste! 🎉")
        break

    # Si no adivinó, damos una pista
    print("Incorrecto... 😢")
    intentos_actuales = intentos_actuales + 1

# Si salimos del bucle sin adivinar
if intentos_actuales >= intentos_maximos:
    print(f"\nGame Over. El número era {numero_secreto}")
```

## La Instrucción continue: El Botón de "Siguiente" ⏭️

### ¿Qué es continue?
continue es como un control remoto que nos permite saltar al siguiente elemento o iteración en nuestro bucle. No termina el bucle como break, solo salta a la siguiente vuelta.

### Ejemplo Práctico: El Verificador de Contraseñas
```python
print("=== Verificador de Contraseñas ===")
print("La contraseña debe tener al menos 8 caracteres")
print("Escribe 'salir' para terminar")

while True:
    # Pedimos una contraseña
    password = input("\nIngresa una contraseña: ")

    # Opción para salir
    if password == "salir":
        print("¡Hasta luego! 👋")
        break

    # Verificamos la longitud
    if len(password) < 8:
        print("❌ Muy corta, intenta otra vez")
        continue

    # Si llegamos aquí, la contraseña es válida
    print("✅ ¡Contraseña válida!")
```

## Ejemplos del Mundo Real 🌎

### 1. El Cajero Automático
```python
saldo = 1000  # Empezamos con $1000

print("=== Cajero Automático ===")
while True:
    # Mostramos el menú
    print(f"\nSaldo actual: ${saldo}")
    print("\n1. Retirar dinero")
    print("2. Salir")

    opcion = input("\nElige una opción (1-2): ")

    # Opción de salir
    if opcion == "2":
        print("Gracias por usar nuestro cajero")
        break

    # Validamos la opción
    if opcion != "1":
        print("Opción no válida")
        continue

    # Pedimos la cantidad a retirar
    retiro = int(input("¿Cuánto deseas retirar?: "))

    # Validamos el retiro
    if retiro > saldo:
        print("No tienes suficiente saldo")
        continue

    # Realizamos el retiro
    saldo = saldo - retiro
    print(f"Retiraste: ${retiro}")
```

### 2. El Validador de Datos
```python
print("=== Validador de Edades ===")
print("Ingresa edades entre 0 y 120")
print("Escribe 'fin' para terminar")

while True:
    # Pedimos una edad
    entrada = input("\nIngresa una edad: ")

    # Verificamos si quiere terminar
    if entrada.lower() == "fin":
        break

    # Intentamos convertir a número
    try:
        edad = int(entrada)
    except ValueError:
        print("❌ Debes ingresar un número")
        continue

    # Validamos el rango
    if edad < 0 or edad > 120:
        print("❌ Edad fuera de rango")
        continue

    # Si llegamos aquí, la edad es válida
    print("✅ Edad válida")
```

## Cuándo Usar Cada Uno 🤔

### break es ideal cuando:
1. Encontramos lo que buscábamos
2. El usuario quiere salir del programa
3. Ocurre una condición especial que requiere terminar
4. Queremos una salida temprana de un bucle

### continue es perfecto para:
1. Saltar casos que no nos interesan
2. Evitar código muy anidado
3. Filtrar elementos que no cumplen ciertos criterios
4. Hacer el código más limpio y eficiente

## Consejos y Buenas Prácticas 💡

1. **Claridad Ante Todo**
   - Usa break y continue cuando hagan el código más claro
   - Documenta por qué los estás usando
   - No abuses de ellos

2. **Mantenibilidad**
   - Evita múltiples break en un mismo bucle
   - Usa continue para reducir la indentación
   - Mantén el código dentro del bucle simple

3. **Seguridad**
   - Siempre verifica condiciones antes de break
   - Usa continue para validación de datos
   - Maneja los casos extremos

# Ejercicios Prácticos: break y continue 🏋️‍♂️

## Ejercicio 1: "El Vendedor Virtual" 🛍️

### Enunciado
Crea un programa que simule una tienda con un presupuesto limitado. El programa debe:
- Comenzar con un presupuesto de $100
- Mostrar productos y sus precios
- Permitir comprar mientras haya presupuesto
- Si no hay suficiente dinero para un producto, saltar a la siguiente iteración
- Terminar cuando el usuario escriba "salir" o se quede sin presupuesto

### Plantilla para Empezar
```python
presupuesto = 100

# Lista de productos disponibles
print("=== TIENDA VIRTUAL ===")
print("Productos disponibles:")
print("1. Camiseta - $25")
print("2. Pantalón - $50")
print("3. Zapatos - $80")
print("Escribe 'salir' para terminar")

# Tu código aquí
```

## Ejercicio 2: "Validador de Claves" 🔐

### Enunciado
Crea un programa que valide claves según estas reglas:
- Debe tener al menos 6 caracteres
- No puede contener espacios
- Debe tener al menos un número
- Máximo 3 intentos por clave
- Si la clave es válida, terminar el programa
- Si la clave es inválida, indicar el error y continuar

### Plantilla para Empezar
```python
print("=== VALIDADOR DE CLAVES ===")
print("Reglas:")
print("- Mínimo 6 caracteres")
print("- Sin espacios")
print("- Al menos un número")
print("Tienes 3 intentos por clave")

# Tu código aquí
```

## 🔍 Soluciones

### Solución Ejercicio 1: "El Vendedor Virtual"
```python
presupuesto = 100

print("=== TIENDA VIRTUAL ===")
print("Productos disponibles:")
print("1. Camiseta - $25")
print("2. Pantalón - $50")
print("3. Zapatos - $80")
print("Escribe 'salir' para terminar")

while True:
    print(f"\nTu presupuesto actual: ${presupuesto}")
    opcion = input("¿Qué deseas comprar? (1-3): ")

    # Verificar si quiere salir
    if opcion == "salir":
        print("¡Gracias por tu compra!")
        break

    # Convertir la opción a precio
    if opcion == "1":
        precio = 25
        producto = "Camiseta"
    elif opcion == "2":
        precio = 50
        producto = "Pantalón"
    elif opcion == "3":
        precio = 80
        producto = "Zapatos"
    else:
        print("Opción no válida")
        continue

    # Verificar si alcanza el presupuesto
    if precio > presupuesto:
        print("No tienes suficiente dinero para este producto")
        continue

    # Realizar la compra
    presupuesto = presupuesto - precio
    print(f"¡Compraste {producto} por ${precio}!")

    # Verificar si quedó sin presupuesto
    if presupuesto == 0:
        print("\n¡Te quedaste sin presupuesto!")
        break
```

### Solución Ejercicio 2: "Validador de Claves"
```python
print("=== VALIDADOR DE CLAVES ===")
print("Reglas:")
print("- Mínimo 6 caracteres")
print("- Sin espacios")
print("- Al menos un número")
print("Tienes 3 intentos por clave")

intentos = 3

while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    clave = input("Ingresa una clave: ")

    # Verificar longitud
    if len(clave) < 6:
        print("❌ Error: La clave debe tener al menos 6 caracteres")
        intentos = intentos - 1
        continue

    # Verificar espacios
    if " " in clave:
        print("❌ Error: La clave no puede contener espacios")
        intentos = intentos - 1
        continue

    # Verificar números
    tiene_numero = False
    for caracter in clave:
        if caracter.isdigit():
            tiene_numero = True
            break

    if not tiene_numero:
        print("❌ Error: La clave debe contener al menos un número")
        intentos = intentos - 1
        continue

    # Si llegamos aquí, la clave es válida
    print("✅ ¡Clave válida!")
    break

if intentos == 0:
    print("\n❌ Se acabaron los intentos")
```

### Explicación de las Soluciones

#### Ejercicio 1:
- Usamos un bucle `while True` para mantener la tienda abierta
- `break` se usa cuando el usuario quiere salir o se queda sin presupuesto
- `continue` se usa cuando la opción no es válida o no hay suficiente dinero
- Mantenemos un seguimiento del presupuesto después de cada compra

#### Ejercicio 2:
- Contamos los intentos disponibles
- Usamos `continue` para cada tipo de error encontrado
- `break` se usa cuando encontramos una clave válida
- Verificamos cada regla por separado para dar mensajes específicos
