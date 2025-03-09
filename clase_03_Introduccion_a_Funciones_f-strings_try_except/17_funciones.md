# Funciones en Python: Fundamentos 🐍

 return "No se puede dividir por cero"

# Uso de la calculadora
print(sumar(10, 5))       # 15
print(restar(10, 5))      # 5
print(multiplicar(10, 5))  # 50
print(dividir(10, 5))     # 2.0
print(dividir(10, 0))     # No se puede dividir por cero
```

### Validador de Datos
```python
def es_numero_valido(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False

def es_correo_valido(correo):
    return '@' in correo and '.' in correo

# Uso de los validadores
print(es_numero_valido("123"))    # True
print(es_numero_valido("abc"))    # False
print(es_correo_valido("user@example.com"))  # True
print(es_correo_valido("invalido"))          # False
```

## Puntos Importantes a Recordar ⭐

1. **Nombres de Funciones**
   - Usar nombres descriptivos
   - Usar snake_case (palabras_separadas_por_guiones)
   - Evitar nombres genéricos

2. **Parámetros**
   - Pueden ser opcionales u obligatorios
   - Pueden tener valores por defecto
   - El orden importa

3. **Return**
   - Una función puede retornar cualquier tipo de dato
   - Si no hay return, la función devuelve None
   - return termina la ejecución de la función

4. **Buenas Prácticas**
   - Una función debe hacer una sola cosa
   - Mantener las funciones cortas y simples
   - Documentar el propósito de la función

## Errores Comunes ⚠️
```python
# ❌ Mal: Función sin dos puntos
def sumar(a, b)
    return a + b

# ✅ Bien: Función con dos puntos
def sumar(a, b):
    return a + b

# ❌ Mal: Indentación incorrecta
def calcular():
print("mal indentado")

# ✅ Bien: Indentación correcta
def calcular():
    print("bien indentado")
```
## ¿Qué es una función? 🤔
Una función es un bloque de código reutilizable que realiza una tarea específica. Imagina una función como una máquina que:
- Puede recibir datos (input)
- Procesa esos datos
- Puede devolver un resultado (output)

### Analogía: La Licuadora 🥤
- La licuadora es como una función
- Los ingredientes son los inputs (parámetros)
- El proceso de licuar es el código dentro de la función
- El batido resultante es el output (return)

## Sintaxis Básica ⚡

### Función Simple
```python
# Definición de una función básica
def saludar():
    print("¡Hola, mundo!")

# Llamada a la función
saludar()  # Imprime: ¡Hola, mundo!
```

### ¿Qué está pasando aquí? 🔍
- `def` indica que estamos definiendo una función
- `saludar` es el nombre de la función
- `()` indica que la función no recibe parámetros
- `:` marca el inicio del bloque de código
- El código indentado pertenece a la función

## Funciones con Parámetros 📥

### Un Parámetro
```python
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

# Llamadas a la función
saludar_persona("Ana")    # Imprime: ¡Hola, Ana!
saludar_persona("Juan")   # Imprime: ¡Hola, Juan!
```

### Múltiples Parámetros
```python
def mostrar_info(nombre, edad):
    print(f"{nombre} tiene {edad} años")

# Llamadas a la función
mostrar_info("María", 25)    # Imprime: María tiene 25 años
mostrar_info("Carlos", 30)   # Imprime: Carlos tiene 30 años
```

## Return: Devolviendo Valores 📤

### Return Simple
```python
def sumar(a, b):
    return a + b

# Uso de la función
resultado = sumar(5, 3)
print(resultado)  # Imprime: 8
```

### Return con Condiciones
```python
def es_mayor_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    return "Eres menor de edad"

# Uso de la función
print(es_mayor_edad(20))  # Imprime: Eres mayor de edad
print(es_mayor_edad(15))  # Imprime: Eres menor de edad
```
#### Diferencia entre print y return
La diferencia principal entre print() y return es su propósito y funcionamiento: print() es una función que muestra información en la pantalla para que la veamos, como un mensaje en la consola, pero no guarda ni devuelve ningún valor que podamos usar después en nuestro código. Por otro lado, return es una instrucción que se usa dentro de funciones para devolver un valor que podemos guardar en una variable y utilizar más tarde en nuestro programa. Para entenderlo mejor, piensa en print() como en una calculadora mostrando un número en su pantalla (solo lo puedes ver), mientras que return sería como la calculadora enviando ese número a otro lugar donde puedes usarlo para más operaciones. Por ejemplo:

```python
def sumar(a, b):
    print(f"El resultado es: {a + b}")  # Solo muestra el resultado

def sumar_con_return(a, b):
    return a + b  # Devuelve el resultado para usarlo después

# Con print() solo vemos el resultado
sumar(2, 3)  # Muestra: El resultado es: 5

# Con return podemos usar el resultado
resultado = sumar_con_return(2, 3)  # Guarda 5 en 'resultado'
resultado_doble = resultado * 2  # Podemos usar el valor devuelto (5 * 2 = 10)
```

Para integrar la sección de scope, sugiero colocarla después de la sección de "Return: Devolviendo Valores" y antes de "Ejemplos Prácticos", expandiéndola así:

## Scope (Alcance) de Variables 🎯

### ¿Qué es el Scope?
El scope o alcance determina en qué partes de nuestro código podemos usar una variable. Es como definir el "territorio" donde una variable existe y puede ser utilizada.

### Variables Locales 📍
Las variables locales solo viven dentro de la función donde se crean:
```python
def calcular_edad():
    edad = 25  # Variable local
    print(f"Dentro de la función: {edad}")

calcular_edad()  # Funciona: imprime 25
# print(edad)    # ¡ERROR! edad no existe fuera de la función

def otra_funcion():
    # print(edad)  # ¡ERROR! edad solo existe en calcular_edad()
    nueva_edad = 30  # Esta es otra variable local diferente
    print(nueva_edad)
```

Las variables locales:
- Solo existen dentro de la función donde se crean
- No se pueden usar fuera de esa función
- Se destruyen cuando la función termina
- Son independientes entre diferentes funciones

### Variables Globales 🌍
Las variables globales están disponibles en todo el programa:
```python
nombre = "Ana"  # Variable global

def saludar():
    print(f"Hola {nombre}")  # Podemos LEER la variable global

def cambiar_nombre():
    global nombre  # Necesario para MODIFICAR la variable global
    nombre = "Juan"

saludar()          # Imprime: Hola Ana
cambiar_nombre()
saludar()          # Imprime: Hola Juan
```

Las variables globales:
- Se crean fuera de cualquier función
- Se pueden leer desde cualquier función
- Para modificarlas dentro de una función, necesitamos la palabra `global`
- Es recomendable limitar su uso

### Ejemplo Práctico de Scope 🎮
```python
puntos = 0  # Variable global para el puntaje del juego

def ganar_puntos():
    global puntos
    puntos = puntos + 10
    print(f"¡Ganaste 10 puntos!")

def perder_puntos():
    global puntos
    puntos = puntos - 5
    print(f"¡Perdiste 5 puntos!")

def mostrar_puntos():
    print(f"Tienes {puntos} puntos")

# Uso del programa
mostrar_puntos()  # Tienes 0 puntos
ganar_puntos()    # ¡Ganaste 10 puntos!
ganar_puntos()    # ¡Ganaste 10 puntos!
perder_puntos()   # ¡Perdiste 5 puntos!
mostrar_puntos()  # Tienes 15 puntos
```

### Consejos sobre Scope 💡
1. Preferir variables locales cuando sea posible
2. Usar variables globales solo cuando sea realmente necesario
3. Tener cuidado al modificar variables globales
4. Dar nombres claros y descriptivos a las variables
5. Pensar en el scope al diseñar funciones


## Ejemplos Prácticos 💡

### Calculadora Básica
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
