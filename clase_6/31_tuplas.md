# Tuplas

Una tupla es una colección de diferentes tipos de datos que está ordenada e inmutable (no se puede cambiar). Las tuplas se escriben con paréntesis `()`. Una vez que se crea una tupla, no podemos cambiar sus valores. No podemos usar métodos como `add`, `insert` o `remove` en una tupla porque no es modificable (es inmutable). A diferencia de las listas, las tuplas tienen pocos métodos. Los métodos relacionados con las tuplas son:

- `tuple()`: para crear una tupla vacía.
- `count()`: para contar el número de veces que aparece un elemento específico en una tupla.
- `index()`: para encontrar el índice de un elemento específico en una tupla.
- Operador `+`: para unir dos o más tuplas y crear una nueva tupla.

### Creación de una tupla

- **Tupla vacía:** Crear una tupla vacía.

  ```py
  # sintaxis
  tupla_vacia = ()
  # o usando el constructor tuple()
  tupla_vacia = tuple()
  ```

- **Tupla con valores iniciales:**

  ```py
  # sintaxis
  tpl = ('item1', 'item2', 'item3')
  ```

  ```py
  frutas = ('banana', 'naranja', 'mango', 'limón')
  ```

### Longitud de una tupla

Usamos el método `len()` para obtener la longitud de una tupla.

```py
# sintaxis
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Acceso a elementos de una tupla

- **Indexación positiva:**
  Similar al tipo de dato lista, usamos indexación positiva o negativa para acceder a los elementos de una tupla.

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3')
  primer_item = tpl[0]
  segundo_item = tpl[1]
  ```

  ```py
  frutas = ('banana', 'naranja', 'mango', 'limón')
  primera_fruta = frutas[0]
  segunda_fruta = frutas[1]
  ultimo_indice = len(frutas) - 1
  ultima_fruta = frutas[ultimo_indice]
  ```

- **Indexación negativa:**
  La indexación negativa comienza desde el final, -1 se refiere al último elemento, -2 al penúltimo y así sucesivamente.

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3', 'item4')
  primer_item = tpl[-4]
  segundo_item = tpl[-3]
  ```

  ```py
  frutas = ('banana', 'naranja', 'mango', 'limón')
  primera_fruta = frutas[-4]
  segunda_fruta = frutas[-3]
  ultima_fruta = frutas[-1]
  ```

### Rebanado (slicing) de tuplas

Podemos extraer una subtupla especificando un rango de índices donde comenzar y terminar. El valor devuelto será una nueva tupla con los elementos especificados.

- **Rango de índices positivos:**

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3', 'item4')
  todos_los_items = tpl[0:4]  # todos los elementos
  todos_los_items = tpl[0:]   # todos los elementos
  dos_items_medios = tpl[1:3] # no incluye el elemento en el índice 3
  ```

  ```py
  frutas = ('banana', 'naranja', 'mango', 'limón')
  todas_las_frutas = frutas[0:4]  # todos los elementos
  todas_las_frutas = frutas[0:]   # todos los elementos
  naranja_mango = frutas[1:3]     # no incluye el elemento en el índice 3
  naranja_hasta_final = frutas[1:]
  ```

- **Rango de índices negativos:**

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3', 'item4')
  todos_los_items = tpl[-4:]      # todos los elementos
  dos_items_medios = tpl[-3:-1]   # no incluye el elemento en el índice -1
  ```

  ```py
  frutas = ('banana', 'naranja', 'mango', 'limón')
  todas_las_frutas = frutas[-4:]  # todos los elementos
  naranja_mango = frutas[-3:-1]   # no incluye el elemento en el índice -1
  naranja_hasta_final = frutas[-3:]
  ```

### Cambiar tuplas a listas

Podemos convertir tuplas en listas y viceversa. Las tuplas son inmutables, por lo que si queremos modificarlas, debemos convertirlas en listas.

```py
# Sintaxis
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
```

```py
frutas = ('banana', 'naranja', 'mango', 'limón')
frutas = list(frutas)
frutas[0] = 'manzana'
print(frutas)     # ['manzana', 'naranja', 'mango', 'limón']
frutas = tuple(frutas)
print(frutas)     # ('manzana', 'naranja', 'mango', 'limón')
```

### Verificar si un elemento está en una tupla

Podemos verificar si un elemento existe o no en una tupla usando `in`, que devuelve un booleano.

```py
# Sintaxis
tpl = ('item1', 'item2', 'item3', 'item4')
'item2' in tpl  # True
```

```py
frutas = ('banana', 'naranja', 'mango', 'limón')
print('naranja' in frutas)  # True
print('manzana' in frutas)  # False
frutas[0] = 'manzana'  # TypeError: 'tuple' object does not support item assignment
```

### Unir tuplas

Podemos unir dos o más tuplas usando el operador `+`.

```py
# sintaxis
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
```

```py
frutas = ('banana', 'naranja', 'mango', 'limón')
vegetales = ('Tomate', 'Papa', 'Repollo', 'Cebolla', 'Zanahoria')
frutas_y_vegetales = frutas + vegetales
```

### Eliminar tuplas

No es posible eliminar un solo elemento de una tupla, pero sí es posible eliminar la tupla completa usando `del`.

```py
# sintaxis
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

```py
frutas = ('banana', 'naranja', 'mango', 'limón')
del frutas
```

🌕 Eres muy valiente, has llegado hasta aquí. Acabas de completar los desafíos del día 6 y estás 6 pasos más cerca de la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios

### Ejercicios: Nivel 1

1. Crea una tupla vacía.
2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien).
3. Une las tuplas de hermanos y hermanas y asígnala a `siblings`.
4. ¿Cuántos hermanos tienes?
5. Modifica la tupla `siblings` y añade el nombre de tu padre y tu madre, luego asígnala a `family_members`.

### Ejercicios: Nivel 2

1. Desempaqueta los hermanos y los padres de `family_members`.
2. Crea tuplas de frutas, vegetales y productos animales. Une las tres tuplas y asígnala a una variable llamada `food_stuff_tp`.
3. Cambia la tupla `food_stuff_tp` a una lista `food_stuff_lt`.
4. Extrae el elemento o elementos del medio de la tupla `food_stuff_tp` o de la lista `food_stuff_lt`.
5. Extrae los primeros tres elementos y los últimos tres elementos de la lista `food_stuff_lt`.
6. Elimina completamente la tupla `food_stuff_tp`.
7. Verifica si un elemento existe en una tupla:
   - Verifica si 'Estonia' es un país nórdico.
   - Verifica si 'Islandia' es un país nórdico.

  ```py
  nordic_countries = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
  ```

---
