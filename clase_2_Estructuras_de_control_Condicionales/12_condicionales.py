# Comparación simple if-elif-else
x = 6
# Estructura condicional que evalúa el valor de x
if x > 5:
  print("X es mayor que 5") # Se ejecuta si x es mayor que 5
elif x == 5:
  print("x es igual que 5") # Se va a  ejecutar si x es igual a 5
else:
  print("X es menor que 5") # Se ejecuta si no se cumple ninguna de las anteriores

print("Estoy fuera de la estructura condicional")


# Combinación de condiciones usando operadores lógicos

x = 8
y = 20

# Usando AND: ambas condiciones deben ser verdaderas:
if x > 10 and y > 25:
  print("Se cumplen las 2 condiciones")

# Usando OR: al menos una de las condiciones se cumple
if x > 10 or y > 25:
  print("Al menos una de las condiciones se cumpe")

# Usando NOT: invierte el valor de la condición
if not x > 10:
  print("X no es mayor que 10")


# Condicionales anidados
is_member = False
age = 19

# Primera condición: verifica si es miembro
if is_member:
  # Condición anidada: solo se evalúa si es miembro
  if age >= 18:
    print("Tienes acceso ya eres miembro y cumples con la edad mínima")
  else:
    print("Aunque seas miembro no cumples con la edad mínima")
else:
  print("No eres miembro y NO TIENES ACCESO")
