# Bucle While 🔄

## 1. ¿Qué es un Bucle While?
Un bucle while es como un guardia que repite una acción mientras una condición sea verdadera. Imagina un juego donde sigues jugando mientras tengas vidas, o una máquina expendedora que sigue funcionando mientras tenga productos.

## 2. Sintaxis Básica
```python
# Estructura básica de un while
while condicion:
    # Código que se ejecutará mientras la condición sea True
    # La condición debe cambiar en algún momento
```

## 3. Ejemplos Simples

### Contador Simple
```python
# Contamos hasta 5
contador = 1
while contador <= 5:
    print(f"Número: {contador}")
    contador = contador + 1
```

### Cuenta Regresiva
```python
# Cuenta regresiva desde 5
cuenta = 5
while cuenta > 0:
    print(f"{cuenta}...")
    cuenta = cuenta - 1
print("¡Despegue! 🚀")
```

## 4. Usos Prácticos

### Ejemplo 1: Adivinar un Número
```python
# Juego simple de adivinanza
numero_secreto = 7
intentos = 3

print("=== Adivina el Número ===")
while intentos > 0:
    print(f"\nTe quedan {intentos} intentos")
    numero = int(input("Adivina el número (1-10): "))

    if numero == numero_secreto:
        print("¡Correcto! 🎉")
        break

    print("Incorrecto...")
    intentos = intentos - 1

if intentos == 0:
    print(f"\nGame Over. El número era {numero_secreto}")
```

### Ejemplo 2: Menú Simple
```python
opcion = ""
while opcion != "3":
    print("\n=== MENÚ ===")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        print("¡Hola! 👋")
    elif opcion == "2":
        print("¡Adiós! 👋")
    elif opcion == "3":
        print("Programa terminado")
    else:
        print("Opción no válida")
```

## 5. While True y Break
A veces queremos un bucle que se ejecute indefinidamente hasta que algo específico ocurra:

```python
print("Calculadora Simple")
print("Escribe 'salir' para terminar")

while True:
    operacion = input("\n¿Qué quieres calcular? ")

    if operacion == "salir":
        print("¡Hasta luego!")
        break

    # Aquí iría el código de la calculadora
    print("Realizando cálculo...")
```

## 6. Diferencias entre While y For
- Usa `while` cuando:
  * No sabes cuántas veces necesitas repetir algo
  * Dependes de una condición que puede cambiar
  * Quieres dar control al usuario para terminar

- Usa `for` cuando:
  * Sabes exactamente cuántas repeticiones necesitas
  * Quieres recorrer una secuencia de elementos
  * Trabajas con range() o listas

# Ejercicios Prácticos: While Loop en Python 🐍

## Ejercicio 1: La Alcancía Digital 💰

### Descripción del Problema
Has decidido ayudar a un amigo a ahorrar dinero creando una alcancía digital. El programa debe ayudar al usuario a alcanzar una meta de ahorro específica.

### Objetivos
- Meta de ahorro: $100
- El usuario puede hacer depósitos de cualquier cantidad
- El programa debe llevar un registro del dinero ahorrado
- Mostrar cuánto se ha ahorrado después de cada depósito
- Celebrar cuando se alcance la meta

### Ejemplo de Ejecución
```
=== Meta de ahorro: $100 ===

¿Cuánto quieres depositar? $30
Tienes ahorrado: $30

¿Cuánto quieres depositar? $50
Tienes ahorrado: $80

¿Cuánto quieres depositar? $20
Tienes ahorrado: $100

¡Felicidades! Alcanzaste tu meta 🎉
```

## Ejercicio 2: El Guardián de la Contraseña 🔐

### Descripción del Problema
Eres el encargado de seguridad de un sistema y necesitas crear un programa que valide contraseñas. El usuario tiene un número limitado de intentos para ingresar la contraseña correcta.

### Objetivos
- Contraseña predefinida: "python123"
- Máximo 3 intentos permitidos
- Mostrar intentos restantes después de cada intento fallido
- Bloquear el acceso después de agotar los intentos
- Conceder acceso inmediato si la contraseña es correcta

### Ejemplo de Ejecución
```
Ingresa la contraseña: abc123
Contraseña incorrecta. Te quedan 2 intentos

Ingresa la contraseña: python456
Contraseña incorrecta. Te quedan 1 intentos

Ingresa la contraseña: python123
¡Acceso concedido! ✅

--- O ---

Ingresa la contraseña: abc123
Contraseña incorrecta. Te quedan 2 intentos

Ingresa la contraseña: def456
Contraseña incorrecta. Te quedan 1 intentos

Ingresa la contraseña: ghi789
Cuenta bloqueada ❌
```

### Conceptos que Practicarás
- Bucles while
- Variables de control
- Condiciones if/else
- Operadores de comparación
- Break para salir del bucle
- Input y output
- Conversión de tipos (int)

### Retos Adicionales
1. **Para la Alcancía:**
   - Agregar un límite máximo por depósito
   - Permitir retiros limitados
   - Calcular cuánto falta para la meta

2. **Para el Validador:**
   - Agregar requisitos de contraseña
   - Implementar tiempo de espera entre intentos
   - Guardar historial de intentos fallidos

### Ejercicio 1: Alcancía
```python
# Programa para ahorrar dinero
meta = 100
ahorros = 0

print(f"=== Meta de ahorro: ${meta} ===")

while ahorros < meta:
    deposito = int(input("\n¿Cuánto quieres depositar? $"))
    ahorros = ahorros + deposito
    print(f"Tienes ahorrado: ${ahorros}")

print("\n¡Felicidades! Alcanzaste tu meta 🎉")
```

### Ejercicio 2: Validador de Contraseña
```python
# Validar contraseña
contrasena_correcta = "python123"
intentos_maximos = 3
intentos = 0

while intentos < intentos_maximos:
    contrasena = input("Ingresa la contraseña: ")

    if contrasena == contrasena_correcta:
        print("¡Acceso concedido! ✅")
        break

    intentos = intentos + 1
    intentos_restantes = intentos_maximos - intentos
    print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos")

if intentos == intentos_maximos:
    print("Cuenta bloqueada ❌")
```

## 8. Tips y Buenas Prácticas
1. Siempre asegúrate de que la condición eventually será False
2. Incluye una forma de salir del bucle
3. Actualiza las variables que afectan la condición
4. Ten cuidado con los bucles infinitos
5. Usa break cuando sea apropiado

## 9. Errores Comunes
1. Olvidar actualizar la condición
2. Condición que nunca se vuelve False
3. Indentación incorrecta
4. No proporcionar una salida del bucle
