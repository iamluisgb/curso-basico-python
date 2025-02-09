# Números enteros (int)
# Los números enteros no tiene parte decimal

numero_entero = 2
numero_negativo = -17
numero_grande = 1_000_0000 # Podemos usar _ para hacer más legibles los números grandes

print("---Enteros---")
print(f"Número entero: {numero_entero}")
print(f"Número negativo: {numero_negativo}")
print(f"Número grande: {numero_grande}")

# Números Decimales (float)
# Los flotantes son números con parte decimal

decimal_simple = 3.14
decimal_negativo = -0.001
decimal_cientifico = 2.5e-3 # Notación científica (2.5 * 10^-3 ? 0.0025) 

print("---Decimales---")
print(f"Número simple: {decimal_simple}")
print(f"Número negativo: {decimal_negativo}")
print(f"Número Cientifico: {decimal_cientifico}")

# Números Complejos (complex)
# Los números complejos tiene parte real y parte imaginaria
numero_complejo = 3 + 4j
otro_complejo = complex(2, -1)

print("---Números complejos---")
print(f"Número Complejo: {numero_complejo}")
print(f"Parte real : {numero_complejo.real}")
print(f"Parte imaginaria : {numero_complejo.imag}")
print(f"Tipo de numero_complejo: {type(numero_complejo)}")