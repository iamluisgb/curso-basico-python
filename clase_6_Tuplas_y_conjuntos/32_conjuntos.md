# Conjuntos (Sets)

Un conjunto es una colección de elementos. Un conjunto es una colección de elementos desordenados y no indexados, donde cada elemento es único. En Python, los conjuntos se utilizan para almacenar elementos únicos, y es posible encontrar la _unión_, _intersección_, _diferencia_, _diferencia simétrica_, _subconjunto_, _superconjunto_ y _conjuntos disjuntos_ entre conjuntos.

### Creación de un Conjunto

Usamos la función incorporada `set()`.

- **Crear un conjunto vacío:**

  ```py
  # sintaxis
  st = set()
  ```

- **Crear un conjunto con elementos iniciales:**

  ```py
  # sintaxis
  st = {'item1', 'item2', 'item3', 'item4'}
  ```

  **Ejemplo:**

  ```py
  frutas = {'banana', 'naranja', 'mango', 'limón'}
  ```

### Obtener la longitud de un conjunto

Usamos el método `len()` para encontrar la longitud de un conjunto.

```py
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Ejemplo:**

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
len(frutas)  # Salida: 4
```

### Acceso a elementos de un conjunto

Usamos bucles para acceder a los elementos de un conjunto. Esto se verá en la sección de bucles.

### Verificar si un elemento existe en un conjunto

Para verificar si un elemento existe en un conjunto, usamos el operador de membresía `in`.

```py
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
print("¿El conjunto st contiene item3? ", 'item3' in st)  # ¿El conjunto st contiene item3? True
```

**Ejemplo:**

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
print('mango' in frutas)  # True
```

### Añadir elementos a un conjunto

Una vez que se crea un conjunto, no podemos cambiar sus elementos, pero sí podemos añadir nuevos elementos.

- **Añadir un elemento usando `add()`:**

  ```py
  # sintaxis
  st = {'item1', 'item2', 'item3', 'item4'}
  st.add('item5')
  ```

  **Ejemplo:**

  ```py
  frutas = {'banana', 'naranja', 'mango', 'limón'}
  frutas.add('lima')
  ```

- **Añadir múltiples elementos usando `update()`:**
  El método `update()` permite añadir múltiples elementos a un conjunto. `update()` toma una lista como argumento.

  ```py
  # sintaxis
  st = {'item1', 'item2', 'item3', 'item4'}
  st.update(['item5', 'item6', 'item7'])
  ```

  **Ejemplo:**

  ```py
  frutas = {'banana', 'naranja', 'mango', 'limón'}
  vegetales = ('tomate', 'papa', 'repollo', 'cebolla', 'zanahoria')
  frutas.update(vegetales)
  ```

### Eliminar elementos de un conjunto

Podemos eliminar un elemento de un conjunto usando el método `remove()`. Si el elemento no se encuentra, `remove()` lanzará un error, por lo que es bueno verificar si el elemento existe en el conjunto. Sin embargo, el método `discard()` no lanza errores.

```py
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

El método `pop()` elimina un elemento aleatorio del conjunto y devuelve el elemento eliminado.

**Ejemplo:**

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
frutas.pop()  # elimina un elemento aleatorio del conjunto
```

Si estamos interesados en el elemento eliminado:

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
elemento_eliminado = frutas.pop()
```

### Limpiar un conjunto

Si queremos vaciar el conjunto, usamos el método `clear()`.

```py
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Ejemplo:**

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
frutas.clear()
print(frutas)  # set()
```

### Eliminar un conjunto

Si queremos eliminar el conjunto completamente, usamos el operador `del`.

```py
# sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Ejemplo:**

```py
frutas = {'banana', 'naranja', 'mango', 'limón'}
del frutas
```

### Convertir una lista a un conjunto

Podemos convertir una lista a un conjunto y viceversa. Convertir una lista a un conjunto elimina los duplicados y solo se conservan los elementos únicos.

```py
# sintaxis
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - el orden es aleatorio, ya que los conjuntos son desordenados
```

**Ejemplo:**

```py
frutas = ['banana', 'naranja', 'mango', 'limón', 'naranja', 'banana']
frutas = set(frutas)  # {'mango', 'limón', 'banana', 'naranja'}
```

### Unir conjuntos

Podemos unir dos conjuntos usando el método `union()` o `update()`.

- **Unión:**
  Este método devuelve un nuevo conjunto.

  ```py
  # sintaxis
  st1 = {'item1', 'item2', 'item3', 'item4'}
  st2 = {'item5', 'item6', 'item7', 'item8'}
  st3 = st1.union(st2)
  ```

  **Ejemplo:**

  ```py
  frutas = {'banana', 'naranja', 'mango', 'limón'}
  vegetales = {'tomate', 'papa', 'repollo', 'cebolla', 'zanahoria'}
  print(frutas.union(vegetales))  # {'limón', 'zanahoria', 'tomate', 'banana', 'mango', 'naranja', 'repollo', 'papa', 'cebolla'}
  ```

- **Actualización:**
  Este método inserta un conjunto en otro.

  ```py
  # sintaxis
  st1 = {'item1', 'item2', 'item3', 'item4'}
  st2 = {'item5', 'item6', 'item7', 'item8'}
  st1.update(st2)  # los contenidos de st2 se añaden a st1
  ```

  **Ejemplo:**

  ```py
  frutas = {'banana', 'naranja', 'mango', 'limón'}
  vegetales = {'tomate', 'papa', 'repollo', 'cebolla', 'zanahoria'}
  frutas.update(vegetales)
  print(frutas)  # {'limón', 'zanahoria', 'tomate', 'banana', 'mango', 'naranja', 'repollo', 'papa', 'cebolla'}
  ```

### Encontrar la intersección de conjuntos

La intersección devuelve un conjunto de elementos que están en ambos conjuntos.

```py
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)  # {'item3', 'item2'}
```

**Ejemplo:**

```py
numeros_enteros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
numeros_enteros.intersection(numeros_pares)  # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)  # {'o', 'n'}
```

### Verificar subconjunto y superconjunto

Un conjunto puede ser un subconjunto o un superconjunto de otros conjuntos:

- **Subconjunto:** `issubset()`
- **Superconjunto:** `issuperset()`

```py
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True
```

**Ejemplo:**

```py
numeros_enteros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
numeros_enteros.issubset(numeros_pares)  # False, porque es un superconjunto
numeros_enteros.issuperset(numeros_pares)  # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)  # False
```

### Verificar la diferencia entre dos conjuntos

Devuelve la diferencia entre dos conjuntos.

```py
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2
```

**Ejemplo:**

```py
numeros_enteros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
numeros_enteros.difference(numeros_pares)  # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)  # {'p', 'y', 't'}  - el resultado es desordenado (característica de los conjuntos)
dragon.difference(python)  # {'d', 'r', 'a', 'g'}
```

### Encontrar la diferencia simétrica entre dos conjuntos

Devuelve la diferencia simétrica entre dos conjuntos. Esto significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A)

```py
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.symmetric_difference(st1)  # {'item1', 'item4'}
```

**Ejemplo:**

```py
numeros_enteros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
algunos_numeros = {1, 2, 3, 4, 5}
numeros_enteros.symmetric_difference(algunos_numeros)  # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### Verificar si dos conjuntos son disjuntos

Si dos conjuntos no tienen elementos en común, se llaman conjuntos disjuntos. Podemos verificar si dos conjuntos son disjuntos usando el método `isdisjoint()`.

```py
# sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)  # False
```

**Ejemplo:**

```py
numeros_pares = {0, 2, 4, 6, 8}
numeros_impares = {1, 3, 5, 7, 9}
numeros_pares.isdisjoint(numeros_impares)  # True, porque no hay elementos comunes

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # False, hay elementos comunes {'o', 'n'}
```

## 💻 Ejercicios

```py
# conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Ejercicios: Nivel 1

1. Encuentra la longitud del conjunto `it_companies`.
2. Añade 'Twitter' a `it_companies`.
3. Inserta múltiples empresas de TI de una vez en el conjunto `it_companies`.
4. Elimina una de las empresas del conjunto `it_companies`.
5. ¿Cuál es la diferencia entre `remove` y `discard`?

### Ejercicios: Nivel 2

1. Une A y B.
2. Encuentra la intersección de A y B.
3. ¿Es A un subconjunto de B?
4. ¿Son A y B conjuntos disjuntos?
5. Une A con B y B con A.
6. ¿Cuál es la diferencia simétrica entre A y B?
7. Elimina los conjuntos completamente.

### Ejercicios: Nivel 3

1. Convierte las edades a un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
2. Explica la diferencia entre los siguientes tipos de datos: string, list, tuple y set.
3. _I am a teacher and I love to inspire and teach people._ ¿Cuántas palabras únicas se han usado en la oración? Usa el método `split` y los conjuntos para obtener las palabras únicas.
