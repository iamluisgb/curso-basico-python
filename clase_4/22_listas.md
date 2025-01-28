# Listas en Python: Una Guía Completa 📝

## 1. ¿Qué es una Lista?
Una lista en Python es como una caja organizada donde podemos guardar múltiples elementos ordenados. Imagina una estantería con libros: cada libro está en una posición específica y podemos acceder a cualquiera conociendo su ubicación.

```python
# Creación de listas
colores = ["rojo", "azul", "verde"]      # Lista de strings
numeros = [1, 2, 3, 4, 5]                # Lista de números
mixta = ["hola", 1, True, 3.14]          # Lista con diferentes tipos de datos
lista_vacia = []                         # Lista sin elementos
```

## 2. Accediendo a Elementos
En Python, las posiciones (índices) empiezan en 0, no en 1. Es como si numeráramos empezando desde 0.

```python
frutas = ["manzana", "banana", "naranja", "pera"]

# Acceso por índice positivo (desde el principio)
primera_fruta = frutas[0]     # manzana
segunda_fruta = frutas[1]     # banana

# Acceso por índice negativo (desde el final)
ultima_fruta = frutas[-1]     # pera
penultima_fruta = frutas[-2]  # naranja

print(f"Primera fruta: {primera_fruta}")
print(f"Última fruta: {ultima_fruta}")
```

## 3. Modificando Listas
Las listas son mutables, lo que significa que podemos cambiar sus elementos después de crearlas.

```python
notas = [85, 90, 78, 95, 88]

# Cambiar un elemento
notas[2] = 80
print(f"Notas actualizadas: {notas}")

# Añadir elementos al final
notas.append(92)
print(f"Después de append: {notas}")

# Remover el último elemento
ultima_nota = notas.pop()
print(f"Nota removida: {ultima_nota}")
print(f"Notas restantes: {notas}")
```

## 4. Operaciones con Listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Unir listas
lista_combinada = lista1 + lista2
print(f"Listas unidas: {lista_combinada}")

# Repetir una lista
lista_repetida = lista1 * 2
print(f"Lista repetida: {lista_repetida}")

# Obtener la longitud
longitud = len(lista1)
print(f"Longitud de lista1: {longitud}")
```

## 5. Rebanadas (Slicing)
Podemos obtener partes de una lista usando rebanadas.

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener los primeros tres números
primeros_tres = numeros[0:3]
print(f"Primeros tres: {primeros_tres}")

# Obtener los últimos tres números
ultimos_tres = numeros[-3:]
print(f"Últimos tres: {ultimos_tres}")

# Obtener números de 2 en 2
cada_dos = numeros[::2]
print(f"Cada dos números: {cada_dos}")
```

## 6. Métodos Útiles de Listas

```python
equipos = ["Real Madrid", "Barcelona", "Sevilla"]

# Agregar al final
equipos.append("Valencia")

# Insertar en una posición específica
equipos.insert(1, "Atlético")

# Remover un elemento específico
equipos.remove("Sevilla")

# Ordenar la lista
equipos.sort()

print(f"Equipos actualizados: {equipos}")
```

## 7. Ejercicios Prácticos

### Ejercicio 1: Lista de Compras
```python
# Crear una lista de compras interactiva
compras = []

# Agregar elementos
item = input("¿Qué necesitas comprar? ")
compras.append(item)
print(f"Lista actual: {compras}")

# Agregar otro elemento
item = input("¿Qué más necesitas? ")
compras.append(item)
print(f"Lista actual: {compras}")

# Eliminar un elemento
eliminar = input("¿Qué producto ya compraste? ")
compras.remove(eliminar)
print(f"Lista actualizada: {compras}")
```

### Ejercicio 2: Calificaciones
```python
# Trabajar con una lista de calificaciones
calificaciones = [85, 90, 78, 95, 88]

# Mostrar la primera y última calificación
print(f"Primera calificación: {calificaciones[0]}")
print(f"Última calificación: {calificaciones[-1]}")

# Modificar una calificación
calificaciones[2] = 80
print(f"Calificaciones actualizadas: {calificaciones}")

# Agregar una nueva calificación
nueva_nota = 92
calificaciones.append(nueva_nota)
print(f"Después de agregar nota: {calificaciones}")
```

## Ejercicios para practicar

### Ejercicio 1: "La Lista de Compras"
Crea una lista de 5 artículos de supermercado. Después:
1. Muestra el primer y último elemento
2. Agrega un nuevo artículo
3. Muestra cuántos artículos hay en total

```python
# Escribe tu solución aquí
```

### Ejercicio 2: "Las Temperaturas"
Tienes una lista con las temperaturas de la semana en grados:
`[21, 24, 19, 25, 22, 20, 23]`

1. Muestra la temperatura más alta
2. Muestra la temperatura más baja
3. Modifica la temperatura del primer día a 18 grados

```python
# Escribe tu solución aquí
```

### Ejercicio 3: "Lista de Amigos"
Crea una lista con los nombres de 4 amigos. Después:
1. Agrega un nuevo amigo al inicio
2. Agrega otro amigo al final
3. Muestra el total de amigos

```python
# Escribe tu solución aquí
```

## Ejercicios Nivel Intermedio 🌿

### Ejercicio 4: "El Torneo"
Tienes una lista de puntajes de un torneo:
`[85, 92, 78, 95, 88]`

1. Muestra los tres primeros puntajes
2. Agrega un nuevo puntaje de 90
3. Muestra los puntajes de manera ordenada

```python
# Escribe tu solución aquí
```

### Ejercicio 5: "Agenda Telefónica"
Crea dos listas: una con nombres y otra con teléfonos:
1. Agrega 3 contactos a cada lista
2. Muestra el teléfono del segundo contacto
3. Agrega un contacto más a ambas listas

```python
# Escribe tu solución aquí
```

## 8. Tips y Consejos
1. Los índices siempre empiezan en 0
2. Podemos usar índices negativos para contar desde el final
3. Las listas pueden contener cualquier tipo de dato
4. Las listas son mutables (podemos cambiarlas)
5. Siempre verifica que el índice existe antes de usarlo


