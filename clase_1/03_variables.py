# ==========================================================
# VARIABLES EN PYTHON
# ==========================================================

nombre = "Luis"
edad = 31
altura = 1.70
es_estudiante = False

# Mostramos los valores y sus tipos
print(f"Nombre: {nombre}, tipo: {type(nombre)}")
print(f"Edad: {edad}, tipo: {type(edad)}")
print(f"Altura: {altura}, tipo: {type(altura)}")
print(f"¿Es estudiante?: {es_estudiante}, tipo: {type(es_estudiante)}")

# Las variables pueden cambiar su valor durante el programa
edad = 28 # cambiamos el valor
print(f"Nueva edad: {edad}")

nombre = "Manuel"
print(f"Nuevo nombre: {nombre}")

# Operaciones entre variables
# Operaciones con números
precio = 100
descuento = 20
precio_final = precio - descuento
print(f"Precio final: {precio_final}")

# Operaciones con strings (texto)
nombre = "Luis"
apellido = "Gonzalez"
nombre_completo = nombre + " " + apellido # Concatenación
print(f"Nombre completo: {nombre_completo}")

# Reglas y convenciones para nombres de variables
nombrePersona = "Juan" # camelCase
nombre_persona = "Belén" # snake_case (recomendado en Python)
VALOR_MAXIMO = 100 # Mayúsculas para constantes

# Nombres NO válidos
# 1variable  = 10   # No se puede empezar con número 
# mi-variable = 20  # No puede contener guiones
# class = 30        # No puede ser una palabra reservada