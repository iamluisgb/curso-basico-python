# ============================================
# STRINGS (CADENAS DE TEXTO) EN PYTHON
# ============================================

print("---CREACIÓN DE STRINGS---")
# Strings con comillas simples o dobles
nombre = 'Luis'
apellido = "Gonzalez"
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")

# La PEP 8 no tiene preferencia, lo importatne la consistencia
mensaje1 = "Don't panic"  # Mejor que: 'Don\'t panic'
print(f"con apóstrofe: {mensaje1}")

# Comillas simples cuando el string contiene comillas dobles
mensaje2 = 'El dijo "Hola"'
print(f"con cita: {mensaje2}")

# Strings multilínea (triple comilla)
mensaje = '''Este es un texto 
que ocupa varias
líneas'''
print(mensaje)

print("---Concatenación de strings---")
# Unir strings con +
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

# Multiplicar un string
separador = "-" * 20
print(separador)

print("---Acceso a caracteres---")
texto = "Python"
print(f"texto: {texto}")
print(f"Primer caracter: {texto[0]}")
print(f"Último caracter: {texto[-1]}")

print(nombre)

nombre = 'Manuel'
edad =  25
altura = 1.75

# Usando format()
print("Me llamo {}, tengo {} años y mido {} metros".format(nombre, edad, altura))

# Usando f-strings (recomendado)
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura} metros")

print("---Acceso a caracteres---")
# \n - nueva línea
# \t - tabulación
# \' - comilla simple
# \" - comilla doble
# \\ - barra invertida
print("Línea 1\nLínea 2")
print("Nombre:\tAna")
print("El dijo: \"Hola\"")