# Convertir datos entre diferentes tipos
print("---Conversiones a string---")

# Número entero a string
numero_entero = 50
texto_desde_entero = str(numero_entero)
print(f"Entero {numero_entero} a string: '{texto_desde_entero}' (tipo: {type(texto_desde_entero)})")

# Número decimal a string
numero_decimal = 3.14
texto_desde_decimal = str(numero_decimal)
print(f"Decimal {numero_decimal} a string: '{texto_desde_decimal}' (tipo: {type(texto_desde_decimal)})")

# Booleano a string
valor_booleano = True
texto_desde_booleano = str(valor_booleano)
print(f"Booleano {valor_booleano} a string: '{texto_desde_booleano}' (tipo: {type(texto_desde_booleano)})")

# -----Conversiones a Entero----
# String a entero
texto_numero = "123"
entero_desde_texto = int(texto_numero)
print(f"String '{texto_numero}' a entero: {entero_desde_texto} (tipo: {type(entero_desde_texto)})")

# Decimal a entero
decimal = 3.7
entero_desde_decimal = int(decimal)
print(f"Decimal {decimal} a entero: {entero_desde_decimal} (tipo: {type(entero_desde_decimal)})")

# ----Conversiones a Decimal---
# String a decimal
texto_decimal = "3.14"
decimal_desde_texto = float(texto_decimal)
print(f"String '{texto_decimal}' a decimal: {decimal_desde_texto} (tipo: {type(decimal_desde_texto)})")

# Entero a decimal
numero = 5
decimal_desde_entero = float(numero)
print(f"Entero {numero} a decimal: {decimal_desde_entero} (tipo: {type(decimal_desde_entero)})")

# ----Casos especiales y errores---
# intentar convertir texto no numérico a número
#numero_invalido = int("abc")
#numero_con_puntos = int("1.23")
numero_con_espacio= int("  123")
