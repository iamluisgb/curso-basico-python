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
