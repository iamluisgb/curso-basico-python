# Valores booleanos
# En python, los booleanos pueden ser True o False
verdadero = True
falso = False
print(f"---Valores Booleanos---")
print(f"Valor Verdadero: {verdadero}")
print(f"Valor Falso: {falso}")

# Booleanos invertidos
verdadero_invertido = not verdadero
falso_invertido = not falso
print(f"---Valores Booleanos invertidos---")
print(f"Valor Verdadero invertido: {verdadero_invertido}")
print(f"Valor Falso invertido: {falso_invertido}")
print(f"Tipo de verdadero invertido: {type(verdadero_invertido)}")

# Doble inversión (vuelve al valor original)
verdadero_doble_invertido = not not verdadero
falso_doble_invertido = not not falso

print(f"---Valores Booleanos con doble inversión---")
print(f"Valor verdadero doblemente invertido: {verdadero_doble_invertido}")
print(f"Valor falso doblemente invertido: {falso_doble_invertido}")