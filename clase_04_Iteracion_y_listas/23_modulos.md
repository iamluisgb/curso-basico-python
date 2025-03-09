# Módulos en Python 📦

## ¿Qué es un Módulo?
Un módulo es un archivo de Python que contiene código (funciones, variables, clases) que puedes reutilizar en otros programas. Los módulos te permiten organizar tu código de manera lógica y evitar repetir código.

## ¿Por qué usar Módulos? 🤔
1. **Reutilización de código**: Escribe el código una vez y úsalo en múltiples programas
2. **Organización**: Mantén tu código ordenado y fácil de mantener
3. **Encapsulación**: Agrupa código relacionado en un solo lugar
4. **Espacio de nombres**: Evita conflictos entre nombres de variables y funciones

## Tipos de Módulos

### 1. Módulos Incorporados (Built-in)
```python
# Ya vienen con Python
import math
import random
import datetime
```

### 2. Módulos de Terceros
```python
# Se instalan con pip
import pandas
import numpy
import requests
```

### 3. Módulos Propios
```python
# Los creas tú mismo
import mi_modulo
import mis_funciones
```

## Cómo Usar Módulos

### 1. Importar un Módulo Completo
```python
import math
resultado = math.sqrt(16)  # 4.0
```

### 2. Importar Elementos Específicos
```python
from math import sqrt
resultado = sqrt(16)  # 4.0
```

### 3. Importar con Alias
```python
import math as m
resultado = m.sqrt(16)  # 4.0
```

## Ejemplos Prácticos

### Usando el Módulo math
```python
import math

# Cálculos matemáticos
raiz = math.sqrt(25)        # Raíz cuadrada
seno = math.sin(0)         # Seno
pi = math.pi               # Valor de Pi
```

### Usando el Módulo random
```python
import random

# Números aleatorios
numero = random.randint(1, 10)     # Número entre 1 y 10
eleccion = random.choice(['A', 'B', 'C'])  # Elige un elemento
```

## Crear tu Propio Módulo

1. **Crea un archivo `mis_funciones.py`:**
```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def sumar(a, b):
    return a + b
```

2. **Úsalo en otro archivo:**
```python
import mis_funciones

print(mis_funciones.saludar("Ana"))
print(mis_funciones.sumar(5, 3))
```

## Consejos y Buenas Prácticas 💡

1. **Importaciones al Inicio**
   - Coloca todos los imports al principio del archivo
   - Organízalos por tipo (built-in, terceros, propios)

2. **Nombres Claros**
   - Usa nombres descriptivos para tus módulos
   - Evita nombres que puedan conflictuar con módulos existentes

3. **Documentación**
   - Documenta tus módulos y funciones
   - Incluye ejemplos de uso

4. **Organización**
   - Agrupa funcionalidades relacionadas en el mismo módulo
   - No hagas módulos demasiado grandes

## Módulos Comunes en Python

1. **math**: Funciones matemáticas
2. **random**: Generación de números aleatorios
3. **datetime**: Manejo de fechas y horas
4. **os**: Interacción con el sistema operativo
5. **sys**: Funcionalidades del sistema
6. **json**: Manejo de datos JSON

## Resumen 📝

Los módulos son una parte fundamental de Python que te permiten:
- Organizar mejor tu código
- Reutilizar funcionalidades
- Acceder a funciones adicionales
- Mantener tu código limpio y ordenado
