# Conversor de monedas de Euros a Dólares
# Pedimos al usuario la cantidad de euros
euros = input("Cuántos euros tienes? ")

# Convertir el texto que ingresó el usuario a decimal
euros = float(euros)

# El valor del euro/dolar
valor_dolar = 0.96

# Conversión
dolares = euros/valor_dolar

# Redondear el resultado a 2 decimales
dolares = round(dolares, 2)

# Mostrar el resultado
print("Tienes $" + str(dolares) + " dólares")
