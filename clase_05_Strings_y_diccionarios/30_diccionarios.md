# Diccionarios en Python: Una Guía Completa 📚

## 1. ¿Qué es un Diccionario?
Imagina un diccionario real - cada palabra (clave/key) tiene su definición (valor/value). En Python, los diccionarios funcionan de manera similar: son estructuras que almacenan información en pares de clave-valor, como una agenda telefónica donde el nombre es la clave y el número es el valor.

## 2. Creando Diccionarios
Hay varias formas de crear un diccionario. Veamos cada una con ejemplos prácticos:

### 2.1 Usando Llaves {}
```python
# La forma más común y directa
estudiante = {
    "nombre": "Ana",
    "edad": 25,
    "curso": "Python"
}
print(estudiante)

# Las claves pueden ser de diferentes tipos
numeros = {
    1: "uno",
    2: "dos",
    3: "tres"
}
```

### 2.2 Usando dict()
```python
# Usando el constructor dict()
contacto = dict(
    nombre="Juan",
    telefono="123456789",
    ciudad="Madrid"
)

# Usando lista de tuplas
contacto2 = dict([
    ("nombre", "María"),
    ("telefono", "987654321"),
    ("ciudad", "Barcelona")
])
```
Algunas propiedades de los diccionario en Python son las siguientes:

- Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
- Son indexados, los elementos del diccionario son accesibles a través del key.
- Y son anidados, un diccionario puede contener a otro diccionario en su campo value.
## 3. Accediendo y Modificando Elementos

### 3.1 Acceso a Valores
```python
estudiante = {
    "nombre": "Ana",
    "edad": 25,
    "curso": "Python"
}

# Dos formas de acceder a los valores
print(estudiante["nombre"])      # Forma directa
print(estudiante.get("nombre"))  # Usando get() (más seguro)

# La diferencia es importante:
# print(estudiante["no_existe"])     # ¡Esto dará error!
print(estudiante.get("no_existe"))   # Retorna None
print(estudiante.get("no_existe", "No encontrado"))  # Valor por defecto
```

### 3.2 Modificando Valores
```python
# Cambiando un valor existente
estudiante["edad"] = 26

# Agregando un nuevo par clave-valor
estudiante["ciudad"] = "Madrid"

print(estudiante)
```

## 4. Operaciones Comunes

### 4.1 Verificando Existencia
```python
estudiante = {"nombre": "Ana", "edad": 25}

# Verificar si una clave existe
if "nombre" in estudiante:
    print("Nombre encontrado:", estudiante["nombre"])

# Verificar si un valor existe
if 25 in estudiante.values():
    print("Hay alguien de 25 años")
```

### 4.2 Eliminando Elementos
```python
estudiante = {
    "nombre": "Ana",
    "edad": 25,
    "curso": "Python",
    "ciudad": "Madrid"
}

# Eliminar un elemento específico
del estudiante["ciudad"]

# Eliminar y obtener el valor
edad = estudiante.pop("edad")

# Eliminar un elemento aleatorio
ultimo_elemento = estudiante.popitem()
```

## 5. Diccionarios Anidados
```python
# Un diccionario puede contener otros diccionarios
escuela = {
    "grupo_a": {
        "profesor": "Juan",
        "estudiantes": ["Ana", "Pedro"]
    },
    "grupo_b": {
        "profesor": "María",
        "estudiantes": ["Luis", "Carmen"]
    }
}

# Accediendo a valores anidados
print(escuela["grupo_a"]["profesor"])
```

## 6. Métodos Útiles

```python
estudiante = {"nombre": "Ana", "edad": 25, "curso": "Python"}

# Obtener todas las claves
print(list(estudiante.keys()))

# Obtener todos los valores
print(list(estudiante.values()))

# Obtener pares clave-valor
print(list(estudiante.items()))

# Copiar un diccionario
estudiante_copia = estudiante.copy()

# Limpiar un diccionario
estudiante.clear()
```

## 7. Ejemplo Práctico: Agenda de Contactos
```python
agenda = {}

# Agregar contactos
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado correctamente")

# Buscar contactos
def buscar_contacto(nombre):
    return agenda.get(nombre, "Contacto no encontrado")

# Uso
agregar_contacto("Ana", "123456789")
agregar_contacto("Juan", "987654321")
print(buscar_contacto("Ana"))
```

## 8. Ejercicios Prácticos

### Ejercicio 1: Generador de Diccionario de Cuadrados 📊

**Descripción del Problema:**
Necesitas crear una función que genere un diccionario donde:
- Las claves sean números consecutivos del 1 hasta n
- Los valores sean los cuadrados de esas claves
- n será el número que el usuario elija

**Ejemplo:**
Si el usuario elige n = 5, el diccionario resultante debería ser:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Datos:**
- Entrada: Un número entero positivo n
- Salida: Un diccionario con números y sus cuadrados

**Ejemplo de Salida:**
```python
Entrada: n = 3
Salida: {1: 1, 2: 4, 3: 9}

Entrada: n = 5
Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Solución:
```python
def generar_diccionario_cuadrados(n):
    """
    Genera un diccionario con números y sus cuadrados.

    Args:
        n: Número hasta donde queremos generar el diccionario

    Returns:
        diccionario: Diccionario con números y sus cuadrados
    """
    # Creamos un diccionario vacío
    diccionario = dict()

    # Iteramos desde 1 hasta n (inclusive)
    for numero in range(1, n + 1):
        # La clave es el número y el valor es su cuadrado
        diccionario[numero] = numero * numero

    return diccionario

# Probamos la función
n = int(input("Ingresa un número: "))
resultado = generar_diccionario_cuadrados(n)
print(f"El diccionario de cuadrados hasta {n} es:")
print(resultado)
```

**Explicación:**
1. La función recibe un número n como parámetro
2. Creamos un diccionario vacío con `dict()`
3. Usando un bucle for, iteramos desde 1 hasta n
4. En cada iteración:
   - La clave es el número actual
   - El valor es ese número multiplicado por sí mismo
5. Finalmente, retornamos el diccionario completo

**Conceptos Aplicados:**
- Creación de diccionarios
- Bucles for con range()
- Asignación de valores a claves en diccionarios
- Input y conversión de tipos


### Ejercicio 2: Convertidor de Calificaciones Numéricas a Categorías 📚

**Descripción del Problema:**
Una escuela necesita convertir las calificaciones numéricas de los estudiantes a categorías cualitativas. Debes crear una función que:
- Reciba un diccionario con los nombres de los estudiantes y sus calificaciones numéricas
- Convierta cada calificación a una categoría según estos criterios:
  * ≥ 85: "Outstanding" (Sobresaliente)
  * ≥ 65: "Good" (Bueno)
  * ≥ 50: "Acceptable" (Aceptable)
  * < 50: "Fail" (Reprobado)
- Retorne un nuevo diccionario con los nombres y sus categorías

**Ejemplo de Entrada:**
```python
calificaciones_estudiantes = {
    "Juan": 90,
    "Ana": 68,
    "María": 88,
    "Carlos": 79,
    "Pedro": 62
}
```

**Ejemplo de Salida:**
```python
{
    "Juan": "Outstanding",
    "Ana": "Good",
    "María": "Outstanding",
    "Carlos": "Good",
    "Pedro": "Good"
}
```

### Solución:
```python
def convertir_calificaciones(calificaciones):
    """
    Convierte calificaciones numéricas a categorías cualitativas.

    Args:
        calificaciones: Diccionario con nombres y calificaciones numéricas

    Returns:
        categorias: Diccionario con nombres y categorías cualitativas
    """
    # Creamos un diccionario vacío para las categorías
    categorias = {}

    # Iteramos sobre cada estudiante y su calificación
    for estudiante, calificacion in calificaciones.items():
        # Asignamos categoría según la calificación
        if calificacion >= 85:
            categorias[estudiante] = "Outstanding"
        elif calificacion >= 65:
            categorias[estudiante] = "Good"
        elif calificacion >= 50:
            categorias[estudiante] = "Acceptable"
        else:
            categorias[estudiante] = "Fail"

    return categorias

# Ejemplo de uso
calificaciones_estudiantes = {
    "Juan": 90,
    "Ana": 68,
    "María": 88,
    "Carlos": 79,
    "Pedro": 62
}

resultado = convertir_calificaciones(calificaciones_estudiantes)
print("Calificaciones convertidas:")
for estudiante, categoria in resultado.items():
    print(f"{estudiante}: {categoria}")
```

**Explicación:**
1. La función recibe un diccionario con calificaciones
2. Creamos un nuevo diccionario para almacenar las categorías
3. Iteramos sobre cada par estudiante-calificación usando .items()
4. Utilizamos condicionales para asignar la categoría correspondiente
5. Guardamos el resultado en el nuevo diccionario
6. Retornamos el diccionario con las categorías

**Conceptos Aplicados:**
- Manipulación de diccionarios
- Iteración sobre diccionarios usando .items()
- Condicionales if/elif/else
- Asignación de valores a diccionarios


### Ejercicio 3: Fusionador de Diccionarios 🔄

**Descripción del Problema:**
Necesitas crear una función que combine dos diccionarios en uno nuevo, donde:
- Se deben mantener todos los elementos de ambos diccionarios
- Si hay claves repetidas, se mantiene el valor del segundo diccionario
- Los diccionarios originales no deben modificarse
- El resultado debe ser un nuevo diccionario

**Ejemplo:**
Si tenemos estos diccionarios:
```python
diccionario1 = {'A': 1, 'B': 2}
diccionario2 = {'B': 3, 'C': 4}
```
El resultado debería ser:
```python
{'A': 1, 'B': 3, 'C': 4}
```

**Datos:**
- Entrada: Dos diccionarios
- Salida: Un nuevo diccionario que combina ambos
- Los diccionarios originales deben permanecer intactos

### Solución:
```python
def combinar_diccionarios(dict1, dict2):
    # Creamos una copia del primer diccionario
    combinado = dict1.copy()

    # Actualizamos con el segundo diccionario
    combinado.update(dict2)

    return combinado

# Ejemplo de uso
diccionario1 = {'Uno': 1, 'Dos': 2, 'Tres': 3}
diccionario2 = {'Tres': 30, 'Cuatro': 4, 'Cinco': 5}

# Combinamos los diccionarios
resultado = combinar_diccionarios(diccionario1, diccionario2)

# Mostramos los resultados
print("Diccionario 1 original:", diccionario1)
print("Diccionario 2 original:", diccionario2)
print("Diccionario combinado:", resultado)
```

**Explicación:**
1. La función recibe dos diccionarios como parámetros
2. Creamos una copia del primer diccionario con .copy()
3. Actualizamos esta copia con el segundo diccionario usando .update()
4. Los valores duplicados se actualizan con los del segundo diccionario
5. Retornamos el nuevo diccionario combinado
6. Los diccionarios originales permanecen sin cambios

**Conceptos Aplicados:**
- Método .copy() para crear una copia de un diccionario
- Método .update() para combinar diccionarios
- Manejo de claves duplicadas
- Preservación de datos originales

## Bonus

### Copia de diccionarios
En Python, el método `.copy()` se usa para hacer una copia **superficial** (*shallow copy*) de un diccionario.


#### ✅ **Ejemplo Básico:**
```python
estudiante = {
    "nombre": "Juan",
    "edad": 21,
    "cursos": ["Matemáticas", "Física"]
}

# Crear una copia del diccionario
estudiante_copia = estudiante.copy()

print(estudiante_copia)
```
**Salida:**
```python
{'nombre': 'Juan', 'edad': 21, 'cursos': ['Matemáticas', 'Física']}
```
📌 Ahora `estudiante_copia` es una copia independiente de `estudiante`.

---

### 🔹 **¿Qué significa "copia superficial"?**
Cuando hacemos `estudiante.copy()`, se copia la **estructura del diccionario**, pero **los valores internos que son mutables (listas, otros diccionarios, etc.) siguen siendo referencias a los mismos objetos**.

#### 🧐 **Ejemplo con Mutabilidad:**
```python
estudiante["cursos"].append("Química")

print(estudiante)
print(estudiante_copia)
```
**Salida:**
```python
{'nombre': 'Juan', 'edad': 21, 'cursos': ['Matemáticas', 'Física', 'Química']}
{'nombre': 'Juan', 'edad': 21, 'cursos': ['Matemáticas', 'Física', 'Química']}
```
🔴 **Problema**: Aunque `estudiante_copia` es una copia del diccionario original, la lista `"cursos"` dentro de ambos sigue siendo la misma.

---

### 🔹 **Cómo hacer una "copia profunda" (Deep Copy)**
Si queremos copiar todo el diccionario **incluyendo los objetos mutables dentro de él**, usamos el módulo `copy` con `deepcopy()`:

```python
import copy

estudiante_copia_profunda = copy.deepcopy(estudiante)

# Ahora modificamos la lista en el original
estudiante["cursos"].append("Historia")

print(estudiante)  # {'nombre': 'Juan', 'edad': 21, 'cursos': ['Matemáticas', 'Física', 'Química', 'Historia']}
print(estudiante_copia_profunda)  # {'nombre': 'Juan', 'edad': 21, 'cursos': ['Matemáticas', 'Física', 'Química']}
```
✅ **Ahora los cambios en `estudiante` no afectan a `estudiante_copia_profunda`**.

---

### 🔹 **Resumen**
| Método | Tipo de Copia | ¿Afecta a datos mutables? |
|--------|-------------|---------------------------|
| `.copy()` | Copia superficial | Sí (objetos mutables se comparten) |
| `copy.deepcopy()` | Copia profunda | No (todo se copia de forma independiente) |

Si el diccionario **solo contiene valores inmutables** (como `int`, `str`, `float`), `copy()` es suficiente. Pero si tiene **listas, diccionarios u otros objetos mutables**, usa `deepcopy()` para evitar efectos no deseados. 🚀
