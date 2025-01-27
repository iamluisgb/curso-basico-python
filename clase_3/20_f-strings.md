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
