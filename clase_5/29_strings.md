# Guía Avanzada de Manipulación de Strings en Python 🎯

Ahora que ya comprendemos los conceptos básicos de strings, vamos a explorar funcionalidades más avanzadas y métodos poderosos que nos permiten manipular texto de forma eficiente.

## 1. Métodos de Transformación

Los strings en Python vienen con métodos incorporados que nos permiten transformar el texto de diferentes maneras:

```python
texto = "  Python Programming  "

# Métodos de cambio de caso
print(texto.upper())          # PYTHON PROGRAMMING
print(texto.lower())          # python programming
print(texto.capitalize())     # Python programming
print(texto.title())         # Python Programming
print(texto.swapcase())      # pYTHON pROGRAMMING

# Métodos de limpieza
print(texto.strip())         # "Python Programming"
print(texto.lstrip())        # "Python Programming  "
print(texto.rstrip())        # "  Python Programming"

# Reemplazo y división
print(texto.replace("P", "J"))  # "  Jython Jrogramming  "
print(texto.split())            # ["Python", "Programming"]
```

## 2. Métodos de Verificación

Podemos verificar diferentes características de nuestros strings:

```python
texto = "Python3.9"
numero = "12345"
espacios = "   "

# Verificaciones de tipo de contenido
print(texto.isalpha())      # False (contiene números)
print(texto.isalnum())      # False (por el .)
print(numero.isdigit())     # True (solo dígitos)
print(espacios.isspace())   # True (solo espacios)

# Verificaciones de caso
texto = "PYTHON"
print(texto.isupper())      # True (todo mayúsculas)
print(texto.islower())      # False
print(texto.istitle())      # False (no es título)
```

## 3. Métodos de Búsqueda y Reemplazo

Python ofrece métodos potentes para encontrar y manipular partes específicas de strings:

```python
texto = "Python es un lenguaje de programación. Python es genial."

# Métodos de búsqueda
print(texto.find("Python"))      # 0 (primera ocurrencia)
print(texto.rfind("Python"))     # 35 (última ocurrencia)
print(texto.count("Python"))     # 2 (número de ocurrencias)
print(texto.startswith("Python")) # True
print(texto.endswith("genial.")) # True

# Reemplazo avanzado
print(texto.replace("Python", "JavaScript", 1))  # Reemplaza solo la primera ocurrencia
```

## 4. Técnicas Avanzadas de Formato

Las f-strings permiten operaciones y expresiones dentro de las llaves:

```python
nombre = "Ana"
edad = 25
puntuacion = 95.7583

# Formato avanzado
print(f"{'=' * 20}")  # Operaciones
print(f"{nombre:>10}")  # Alineación a la derecha
print(f"{nombre:<10}")  # Alineación a la izquierda
print(f"{nombre:^10}")  # Centrado

# Formato de números
print(f"{puntuacion:.2f}")  # Dos decimales
print(f"{edad:03d}")        # Relleno con ceros
print(f"{edad:+}")          # Mostrar signo
```

## 5. Particionado y Unión

```python
texto = "Python,Java,JavaScript"
correo = "usuario@dominio.com"

# Particionado
lenguajes = texto.split(",")    # ['Python', 'Java', 'JavaScript']
usuario, dominio = correo.split("@")  # Desempaquetado

# Unión
nuevo_texto = " | ".join(lenguajes)  # Python | Java | JavaScript
```

## 6. Aplicaciones Prácticas

### Procesamiento de Texto
```python
def limpiar_texto(texto):
    """Limpia y estandariza un texto"""
    # Eliminar espacios extra y convertir a minúsculas
    texto = texto.strip().lower()

    # Reemplazar múltiples espacios por uno solo
    texto = " ".join(texto.split())

    # Eliminar caracteres especiales
    caracteres_especiales = "!@#$%^&*()_+"
    for caracter in caracteres_especiales:
        texto = texto.replace(caracter, "")

    return texto

# Ejemplo de uso
texto_sucio = "  Python  @  Programming!  "
texto_limpio = limpiar_texto(texto_sucio)
print(texto_limpio)  # "python programming"
```

### Validación de Formato
```python
def validar_correo(correo):
    """Valida el formato básico de un correo electrónico"""
    correo = correo.strip()

    # Verificaciones básicas
    if not "@" in correo:
        return False
    if not "." in correo:
        return False

    # Verificar formato usuario@dominio.com
    partes = correo.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio = partes
    return len(usuario) > 0 and "." in dominio
```
