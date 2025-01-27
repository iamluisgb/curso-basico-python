# Funciones Incorporadas (Built-in Functions) en Python 🐍

## Introducción
Las funciones incorporadas (built-in functions) son funciones que vienen pre-instaladas con Python y están disponibles para su uso inmediato sin necesidad de importar ningún módulo. Estas funciones proporcionan funcionalidades básicas y esenciales que se utilizan frecuentemente en la programación con Python.

Estas funciones son parte del núcleo del lenguaje y puedes usarlas en cualquier momento sin necesidad de configuración adicional. Para usar una función incorporada, simplemente necesitas llamarla por su nombre.

## Lista de Funciones Incorporadas

### Funciones Numéricas
| Función | Descripción |
|---------|-------------|
| abs() | Devuelve el valor absoluto de un número |
| float() | Convierte a número decimal |
| int() | Convierte a número entero |
| max() | Devuelve el elemento más grande de un iterable |
| min() | Devuelve el elemento más pequeño de un iterable |
| pow() | Devuelve el valor de x elevado a la potencia y |
| round() | Redondea un número |
| sum() | Suma los elementos de un iterable |

### Funciones de Conversión
| Función | Descripción |
|---------|-------------|
| bin() | Convierte un número a binario |
| hex() | Convierte un número a hexadecimal |
| oct() | Convierte un número a octal |
| str() | Convierte a cadena de texto |
| bool() | Convierte al valor booleano del objeto especificado |

### Funciones de Entrada/Salida
| Función | Descripción |
|---------|-------------|
| input() | Permite la entrada de usuario |
| print() | Imprime en la salida estándar |
| open() | Abre un archivo y devuelve un objeto archivo |

### Funciones de Utilidad
| Función | Descripción |
|---------|-------------|
| len() | Devuelve la longitud de un objeto |
| type() | Devuelve el tipo de un objeto |
| help() | Ejecuta el sistema de ayuda incorporado |
| format() | Da formato a un valor especificado |
| id() | Devuelve el identificador de un objeto |

### Funciones de Secuencia
| Función | Descripción |
|---------|-------------|
| range() | Devuelve una secuencia de números |
| reversed() | Devuelve un iterador invertido |
| sorted() | Devuelve una lista ordenada |
| list() | Devuelve una lista |
| tuple() | Devuelve una tupla |
| set() | Devuelve un nuevo conjunto |

### Funciones Avanzadas
| Función | Descripción |
|---------|-------------|
| eval() | Evalúa y ejecuta una expresión |
| exec() | Ejecuta el código especificado |
| filter() | Filtra elementos en un objeto iterable |
| map() | Aplica una función a cada elemento de un iterable |
| zip() | Devuelve un iterador de tuplas combinando varios iterables |

## Nota Importante
No es necesario memorizar todas estas funciones. A medida que vayas programando, te familiarizarás con las más comunes y podrás consultar la documentación para las demás cuando las necesites.

## Referencias
- Para más información sobre cualquier función, puedes usar `help(nombre_funcion)` en Python
- La documentación oficial de Python proporciona ejemplos detallados de cada función
- Es recomendable practicar con ejemplos simples para entender mejor cada función

## Ejercicios Básicos

### 1. Jugando con Números
```python
# Crear un programa que:
# - Pida un número al usuario
# - Muestre su valor absoluto
# - Muestre su valor redondeado
# - Muestre su tipo

numero = float(input("Ingresa un número (puede ser negativo y/o decimal): "))
print(f"Valor absoluto: {abs(numero)}")
print(f"Valor redondeado: {round(numero)}")
print(f"Tipo de dato: {type(numero)}")
```

### 2. Conversor de Tipos
```python
# Pide al usuario su edad y su altura
# Muestra qué tipo de dato es cada uno antes y después de la conversión

edad = input("¿Cuál es tu edad? ")
altura = input("¿Cuál es tu altura en metros? ")

print(f"\nAntes de convertir:")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de altura: {type(altura)}")

edad = int(edad)
altura = float(altura)

print(f"\nDespués de convertir:")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de altura: {type(altura)}")
```

### 3. Calculadora de Máximos y Mínimos
```python
# Pide tres números y encuentra:
# - El mayor
# - El menor
# - La suma de todos

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
suma = sum([num1, num2, num3])

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"La suma de todos es: {suma}")
```

### 4. Comprobador de Tipos
```python
# Muestra diferentes tipos de valores y comprueba su tipo

valor1 = "Hola"
valor2 = 123
valor3 = 3.14
valor4 = True

print(f"'{valor1}' es de tipo: {type(valor1)}")
print(f"{valor2} es de tipo: {type(valor2)}")
print(f"{valor3} es de tipo: {type(valor3)}")
print(f"{valor4} es de tipo: {type(valor4)}")
```

### 5. Conversor de Valores Booleanos
```python
# Comprueba qué valores se convierten a True y cuáles a False

print("Convertir a booleano:")
print(f"bool('Hola'): {bool('Hola')}")
print(f"bool(''): {bool('')}")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(-10): {bool(-10)}")
```
