# Operadores de comparación
# Estos operadores retornan valores booleanos
a = 5
b = 10

print("---Operadores de comparación---")
print(f"a = {a}, b = {b}")
print(f"Igual a (==): {a} == {b} es {a == b}")
print(f"Diferente de (!=): {a} != {b} es {a != b}")
print(f"Menor que (<): {a} < {b} es {a < b}")
print(f"Mayor que (>): {a} > {b} es {a > b}")
print(f"Menor o igual (<=): {a} <= {b} es {a <= b}")
print(f"Mayor o igual (>=): {a} >= {b} es {a >= b}")

# Operadores lógicos
x = True
y = False

print("\n=== Operadores Lógicos ===")
print(f"x = {x}, y = {y}")
print(f"AND (x and y): {x and y}")  # True solo si ambos son True
print(f"OR (x or y): {x or y}")     # True si al menos uno es True
print(f"NOT x: {not x}")            # Invierte el valor booleano

# Valores que siempre se evalúan como False
print("\n=== Valores Falsy ===")
print(f"Bool de cadena vacía: {bool('')}")
print(f"Bool de cero: {bool(0)}")
print(f"Bool de None: {bool(None)}")
print(f"Bool de lista vacía: {bool([])}")
print(f"Bool de tupla vacía: {bool(())}")
print(f"Bool de diccionario vacío: {bool({})}")

# Valores que siempre se evalúan como True
print("\n=== Valores Truthy ===")
print(f"Bool de cadena no vacía: {bool('Hola')}")
print(f"Bool de número diferente de cero: {bool(42)}")
print(f"Bool de lista no vacía: {bool([1, 2, 3])}")
print(f"Bool de True: {bool(True)}")

# Operaciones encadenadas
# Ejemplo con número simple
num = 5
print("\n=== Operaciones Encadenadas con un Número ===")
print(f"0 <= {num} <= 10: {0 <= num <= 10}")  # Verifica si num está entre 0 y 10
print(f"0 <= {num} <= 3: {0 <= num <= 3}")    # Verifica si num está entre 0 y 3
print(f"-5 < {num} < 7: {-5 < num < 7}")      # Verifica si num está entre -5 y 7
print(f"1 < {num} > 3: {1 < num > 3}")        # Verifica si num es mayor que 1 Y mayor que 3

# Ejemplo con múltiples números
a, b, c = 3, 5, 7
print("\n=== Operaciones Encadenadas con Múltiples Números ===")
print(f"{a} < {b} < {c}: {a < b < c}")        # Verifica si los números están en orden ascendente
print(f"{c} > {b} > {a}: {c > b > a}")        # Verifica si los números están en orden descendente
print(f"{a} <= {b} <= {c}: {a <= b <= c}")    # Verifica orden ascendente o igual
print(f"{a} < {b} > {a}: {a < b > a}")        # Verifica si b es mayor que a

# Comparaciones más complejas
x = 10
print("\n=== Operaciones Encadenadas Complejas ===")
print(f"5 <= {x} <= 15 <= 20: {5 <= x <= 15 <= 20}")  # Múltiples condiciones
print(f"0 <= {x} <= 100 >= 50 >= 25: {0 <= x <= 100 >= 50 >= 25}")

# Comparaciones con diferentes operadores
valor = 7
print("\n=== Operaciones Encadenadas con Diferentes Operadores ===")
print(f"1 < {valor} < 10 != 5: {1 < valor < 10 != 5}")  # Combina <, != en una cadena
print(f"0 <= {valor} <= 10 == 10: {0 <= valor <= 10 == 10}")  # Combina <=, == en una cadena

# Ejemplos de casos prácticos
edad = 25
precio = 50

print(f"Edad entre 18 y 30 y el precio es menor a 100 { 18 <= edad <= 30 and 0 <= precio <= 100}")

# Temperatura confortable (18-25)
temperatura = 23
print(f"Temperatura: {temperatura}, está entre 18 y 25 {18 < temperatura < 25}")

print("---Operador is vs == ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
# 'is'  compara la identidad, '==' compara el valor

print("\n=== Operador is vs == ===")
print(f"a == b: {a == b}")  # True porque tienen el mismo valor
print(f"a is b: {a is b}")  # False porque son objetos diferentes
print(f"a is c: {a is c}")  # True porque c es una referencia a a

# Patrones comunes con booleanos
nombre = ""
valor_predeterminado = "Usuario"

print("---Patrones comunes---")
nombre_mostrar = nombre or valor_predeterminado
print(f"Nombre a mostrar: {nombre_mostrar}")

# Usar para verificación segura
lista = [1,2,3]
# Solo intenta acceder al índice si la lista tiene elementos
elemento = lista and lista[0]
print(f"Primer elemento: {elemento}")