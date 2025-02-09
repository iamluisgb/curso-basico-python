# F-strings en Python
## Formato Moderno y Legible de Strings

### 1. ¿Qué son las f-strings?
Las f-strings (formatted string literals) son una forma moderna y legible de formatear strings en Python. Se introdujeron en Python 3.6 y son la manera recomendada de formatear strings.

### 2. Sintaxis Básica
```python
# Forma básica de f-strings
nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años")

# Comparación con forma tradicional
print("Me llamo " + nombre + " y tengo " + str(edad) + " años")  # Antigua
print(f"Me llamo {nombre} y tengo {edad} años")                  # Nueva (f-string)
```

### 3. Ejemplos Prácticos

#### Números y Operaciones Matemáticas
```python
# Las f-strings pueden incluir operaciones matemáticas
base = 5
altura = 3
print(f"El área del rectángulo es {base * altura}")

# Redondeo de números
precio = 19.99999
print(f"El precio es ${precio:.2f}")  # Muestra: El precio es $20.00
```

#### Formateo de Números
```python
# Números con comas como separadores de miles
numero_grande = 1234567
print(f"Número formateado: {numero_grande:,}")  # Muestra: 1,234,567

# Porcentajes
porcentaje = 0.19544
print(f"Porcentaje: {porcentaje:.1%}")  # Muestra: 19.5%
```

#### Alineación y Espaciado
```python
# Alineación de texto
nombre = "Juan"
print(f"|{nombre:<10}|")  # Alineado a la izquierda
print(f"|{nombre:>10}|")  # Alineado a la derecha
print(f"|{nombre:^10}|")  # Centrado

# Resultado:
# |Juan      |
# |      Juan|
# |   Juan   |
```

### 4. Ejercicios Prácticos

#### Ejercicio 1: Información Personal
```python
# Crea un perfil usando f-strings
nombre = "Carlos"
edad = 30
ciudad = "Madrid"
profesion = "programador"

print(f"""
=== PERFIL ===
Nombre: {nombre}
Edad: {edad} años
Ciudad: {ciudad}
Profesión: {profesion}
""")
```

#### Ejercicio 2: Calculadora con Formato
```python
# Muestra operaciones matemáticas con formato
num1 = 15
num2 = 7

print(f"""
Operaciones entre {num1} y {num2}:
Suma: {num1 + num2}
Resta: {num1 - num2}
Multiplicación: {num1 * num2}
División: {num1 / num2:.2f}
""")
```

#### Ejercicio 3: Tabla de Productos
```python
# Crear una tabla formateada de productos
producto1 = "Manzanas"
precio1 = 2.5
producto2 = "Peras"
precio2 = 3.75

print(f"""
{'PRODUCTO':<10} | {'PRECIO':>7}
{'-'*10} | {'-'*7}
{producto1:<10} | ${precio1:>6.2f}
{producto2:<10} | ${precio2:>6.2f}
""")
```

### 5. Ventajas de f-strings
1. Más legibles y mantenibles
2. Menos propensos a errores
3. Mejor rendimiento
4. Sintaxis más concisa
5. Permiten expresiones dentro de las llaves

### 6. Tips y Trucos

#### Debug de Variables
```python
# Mostrar nombre y valor de variables
x = 42
print(f"{x=}")  # Muestra: x=42

# Múltiples variables
y = 100
print(f"{x=}, {y=}")  # Muestra: x=42, y=100
```

#### Formato de Números
```python
# Diferentes formatos numéricos
numero = 123456.789
print(f"Normal: {numero}")
print(f"Comas: {numero:,}")
print(f"Exponencial: {numero:e}")
print(f"Porcentaje: {numero:.2%}")
```

### 7. Errores Comunes a Evitar
- Olvidar la 'f' antes del string
- Confundir la sintaxis con otros métodos de formato
- No cerrar las llaves correctamente
- Usar comillas incorrectamente dentro de las f-strings

### 8. Ejercicios para Practicar
#### Ejercicio 1: Generador de recibos
**Objetivo:** Crear un programa que genere un recibo de compra formateado para una tienda.

**Requisitos:**
1. El programa debe mostrar:
   - Nombre de la tienda centrado
   - Una tabla con columnas para: Producto, Precio, Cantidad y Total
   - Líneas separadoras para mejor legibilidad
   - Total final
   - Mensaje de agradecimiento

2. Formato requerido:
   - Precios con dos decimales
   - Columnas alineadas correctamente
   - Símbolos de moneda ($)
   - Bordes usando caracteres especiales (=, -)

**Ejemplo de salida esperada:**
```
          TIENDA DE ROPA
========================================
Producto        Precio  Cant   Total
----------------------------------------
Camiseta       $25.99     2  $51.98
Pantalón       $49.99     1  $49.99
Calcetines      $5.99     3  $17.97
----------------------------------------
TOTAL:                      $119.94

       ¡Gracias por su compra!
```
#### Solución
```python
# Datos de los productos
producto1 = "Camiseta"
precio1 = 25.99
cantidad1 = 2

producto2 = "Pantalón"
precio2 = 49.99
cantidad2 = 1

producto3 = "Calcetines"
precio3 = 5.99
cantidad3 = 3

# Calculamos los subtotales
subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3

# Calculamos el total
total = subtotal1 + subtotal2 + subtotal3

# Imprimimos el recibo formateado
print(f"""
{"TIENDA DE ROPA":^40}
{"=" * 40}

{"Producto":<15}{"Precio":>8}{"Cant":>8}{"Total":>9}
{"-" * 40}
{producto1:<15}${precio1:>7.2f}{cantidad1:>8}${subtotal1:>8.2f}
{producto2:<15}${precio2:>7.2f}{cantidad2:>8}${subtotal2:>8.2f}
{producto3:<15}${precio3:>7.2f}{cantidad3:>8}${subtotal3:>8.2f}
{"-" * 40}
{"TOTAL:":<31}${total:>8.2f}

{"¡Gracias por su compra!":^40}
""")
```

#### Ejercicio 2: Tabla de Multiplicar Formateada 📊
**Objetivo:** Crear un programa que muestre una tabla de multiplicar con formato profesional.

**Requisitos:**
1. El programa debe:
   - Pedir al usuario un número
   - Mostrar la tabla del 1 al 10 para ese número
   - Incluir un encabezado decorativo
   - Alinear todos los números correctamente

2. Formato requerido:
   - Números alineados a la derecha
   - Separadores visuales
   - Título centrado

**Ejemplo de salida esperada:**
```
======= Tabla del 7 =======
 7 x  1 =   7
 7 x  2 =  14
 7 x  3 =  21
 7 x  4 =  28
 7 x  5 =  35
 7 x  6 =  42
 7 x  7 =  49
 7 x  8 =  56
 7 x  9 =  63
 7 x 10 =  70
==========================
```

#### Solución
```python
# Pedimos el número para la tabla
numero = int(input("¿Qué tabla de multiplicar quieres ver? "))

# Imprimimos el encabezado
print(f"\n{f' Tabla del {numero} ':=^30}")

# Generamos la tabla
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero:2} x {i:2} = {resultado:3}")

print("=" * 30)
```

#### Ejercicio 3: Informe Meteorológico 🌤️
**Objetivo:** Crear un programa que muestre un informe del tiempo con formato profesional.

**Requisitos:**
1. El programa debe mostrar:
   - Nombre de la ciudad
   - Temperatura en grados Celsius
   - Porcentaje de humedad
   - Probabilidad de lluvia
   - Velocidad y dirección del viento

2. Formato requerido:
   - Usar emojis para los diferentes indicadores
   - Temperatura con un decimal
   - Probabilidad de lluvia en porcentaje
   - Indicadores visuales del estado del tiempo
   - Hora de generación del informe

**Ejemplo de salida esperada:**
```
        INFORME METEOROLÓGICO
========================================
🌍 Ciudad: Madrid
🌡️ Temperatura:  22.5°C
💧 Humedad:      65%
🌧️ Prob. lluvia:   35%
🌪️ Viento:     12 km/h NE

Estado del tiempo:
----------------------------------------
Temperatura:    😊
Humedad:        👍
Lluvia:         ☔

Pronóstico generado a las 15:30
```

#### Solución
```python
from datetime import datetime

# Datos meteorológicos
ciudad = "Madrid"
temperatura = 22.5
humedad = 65
prob_lluvia = 0.35
velocidad_viento = 12
direccion_viento = "NE"

# Creamos el informe meteorológico
print(f"""
{"INFORME METEOROLÓGICO":^40}
{"=" * 40}

🌍 Ciudad: {ciudad}
🌡️ Temperatura: {temperatura:>5.1f}°C
💧 Humedad: {humedad:>8}%
🌧️ Prob. lluvia: {prob_lluvia:>6.0%}
🌪️ Viento: {velocidad_viento:>4} km/h {direccion_viento}

Estado del tiempo:
{'-' * 40}
{'Temperatura:':<15} {"🥶" if temperatura < 15 else "😊" if temperatura < 25 else "🥵"}
{'Humedad:':<15} {"👍" if 30 <= humedad <= 70 else "👎"}
{'Lluvia:':<15} {"☔" if prob_lluvia > 0.3 else "☀️"}

{"Pronóstico generado a las " + datetime.now().strftime('%H:%M')}
""")
```
