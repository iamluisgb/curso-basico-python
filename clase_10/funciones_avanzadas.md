# Funciones Avanzadas en Python

## 1. Explicación Teórica

### 1.1 Introducción y Motivación

Imagina que eres un chef en una cocina. Cuando empezaste, aprendiste a hacer platos básicos siguiendo recetas exactas: una cantidad específica de cada ingrediente, en un orden específico. Esto es similar a las funciones básicas que hemos aprendido hasta ahora:

```python
def hacer_sandwich(pan, queso, jamon):
    return f"Sandwich de {pan} con {queso} y {jamon}"
```

Pero a medida que te vuelves más experto, aprendes a ser más flexible: algunos ingredientes son opcionales, puedes añadir extras, o incluso crear platos completamente personalizados según los ingredientes disponibles. Las funciones avanzadas en Python nos permiten esta misma flexibilidad.

### 1.2 Fundamentos Clave

En esta clase aprenderemos tres conceptos fundamentales:

1. **Parámetros Flexibles**: Diferentes formas de pasar información a nuestras funciones
2. **Args y Kwargs**: Cómo hacer funciones que acepten cualquier cantidad de argumentos
3. **Recursividad**: Una técnica donde una función se llama a sí misma

### 1.3 Analogías y Ejemplos Conceptuales

Para entender mejor estos conceptos, usaremos analogías de la vida real:

1. **Parámetros por Defecto**: Como un restaurante de hamburguesas
   - Hay una receta estándar (valores por defecto)
   - Puedes personalizar ingredientes (cambiar valores)
   - Algunos ingredientes son opcionales

2. **Args y Kwargs**: Como una mochila
   - Args (*args): Puedes meter cualquier cantidad de objetos
   - Kwargs (**kwargs): Cada objeto tiene una etiqueta con su nombre

3. **Recursividad**: Como buscar un libro en una biblioteca
   - Empiezas en una sección
   - Si no está allí, buscas en la siguiente
   - Repites hasta encontrarlo

## 2. Código de Demostración

### 2.1 Ejemplo Básico: Parámetros Flexibles
```python
def crear_perfil(nombre, edad=None, ciudad="Desconocida"):
    """
    Crea un perfil de usuario con diferentes niveles de información

    Args:
        nombre: Nombre del usuario (obligatorio)
        edad: Edad del usuario (opcional)
        ciudad: Ciudad del usuario (opcional, valor por defecto)
    """
    perfil = f"Nombre: {nombre}"

    if edad is not None:  # Solo añadimos edad si se proporcionó
        perfil += f"\nEdad: {edad} años"

    perfil += f"\nCiudad: {ciudad}"
    return perfil

# Ejemplos de uso
print("Perfil básico:")
print(crear_perfil("Ana"))

print("\nPerfil con edad:")
print(crear_perfil("Juan", edad=25))

print("\nPerfil completo:")
print(crear_perfil("María", 30, "Madrid"))
```

### 2.3 Args y Kwargs: La Flexibilidad en Python

#### *args: Argumentos Posicionales Variables
Imagina que tienes una caja mágica que puede contener cualquier cantidad de objetos. En Python, `*args` es esa caja mágica para nuestras funciones.

```python
def suma_todos(*numeros):
    """
    Suma cualquier cantidad de números

    Args:
        *numeros: Tupla con todos los números a sumar

    Returns:
        float: La suma de todos los números
    """
    total = 0
    print("Números recibidos:", numeros)  # Para ver qué recibimos

    for numero in numeros:
        total += numero
        print(f"Sumando {numero}: total actual = {total}")

    return total

# Ejemplos de uso
print("\nSumando dos números:")
print(suma_todos(5, 10))

print("\nSumando cinco números:")
print(suma_todos(1, 2, 3, 4, 5))

print("\nSumando un solo número:")
print(suma_todos(100))
```

#### **kwargs: Argumentos Nombrados Variables
Si `*args` es una caja mágica, `**kwargs` es como un archivador donde cada objeto tiene una etiqueta.

```python
def crear_ficha_persona(**datos):
    """
    Crea una ficha de persona con cualquier cantidad de información

    Args:
        **datos: Diccionario con la información de la persona

    Returns:
        str: Ficha formateada
    """
    print("Datos recibidos:", datos)  # Para ver qué recibimos

    ficha = "=== FICHA PERSONAL ===\n"

    # Procesamos cada dato recibido
    for campo, valor in datos.items():
        ficha += f"{campo.title()}: {valor}\n"

    return ficha

# Ejemplos de uso
print(crear_ficha_persona(
    nombre="Ana",
    edad=25,
    ciudad="Madrid"
))

print(crear_ficha_persona(
    nombre="Juan",
    profesion="Programador",
    lenguaje_favorito="Python",
    años_experiencia=3
))
```

#### Combinando Args y Kwargs
Podemos usar ambos en la misma función:

```python
def registrar_estudiante(*materias, **datos_personales):
    """
    Registra un estudiante con sus materias y datos personales

    Args:
        *materias: Lista de materias que cursa
        **datos_personales: Información personal del estudiante
    """
    registro = f"=== REGISTRO DE ESTUDIANTE ===\n"

    # Añadir información personal
    for campo, valor in datos_personales.items():
        registro += f"{campo.title()}: {valor}\n"

    # Añadir materias
    registro += "\nMaterias inscritas:\n"
    for i, materia in enumerate(materias, 1):
        registro += f"{i}. {materia}\n"

    return registro

# Ejemplo de uso
print(registrar_estudiante(
    "Matemáticas", "Física", "Programación",  # args
    nombre="Pedro",                           # kwargs
    edad=20,
    semestre=3
))
```

### 2.4 Recursividad: Funciones que se Llaman a Sí Mismas

La recursividad es como un espejo frente a otro espejo: la imagen se repite una y otra vez. En programación, es cuando una función se llama a sí misma para resolver un problema.

#### Ejemplo Básico: Cuenta Regresiva
```python
def cuenta_regresiva(n):
    """
    Realiza una cuenta regresiva desde n hasta 0

    Args:
        n: Número desde donde empezar la cuenta
    """
    # Caso base: cuando parar
    if n <= 0:
        print("¡Despegue! 🚀")
        return

    # Mostrar número actual
    print(n)

    # Llamada recursiva
    cuenta_regresiva(n - 1)

# Ejemplo de uso
cuenta_regresiva(5)
```

#### Ejemplo Práctico: Factorial
```python
def factorial(n):
    """
    Calcula el factorial de un número usando recursividad

    Args:
        n: Número del que calcular el factorial

    Returns:
        int: El factorial de n
    """
    # Mostramos el proceso
    print(f"Calculando factorial de {n}")

    # Caso base
    if n <= 1:
        print(f"factorial(1) = 1")
        return 1

    # Llamada recursiva
    resultado = n * factorial(n - 1)
    print(f"factorial({n}) = {n} * factorial({n-1}) = {resultado}")
    return resultado

# Ejemplo de uso con explicación paso a paso
resultado = factorial(5)
print(f"\nEl factorial de 5 es {resultado}")
```


## 3. Ejemplos Prácticos

### 3.1 Lista de Compras Flexible
```python
def crear_lista_compras(*items, tienda="supermercado"):
    """
    Crea una lista de compras que puede tener cualquier número de items

    Args:
        *items: Items para comprar
        tienda: Lugar donde comprar (opcional)
    """
    print(f"Lista de compras para {tienda}:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

# Diferentes formas de usar la función
crear_lista_compras("pan", "leche")
print()  # Separador
crear_lista_compras("manzanas", "peras", "plátanos", tienda="frutería")
```

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico
**Ejercicio: Calculadora Flexible**
- Crear una función que pueda sumar cualquier cantidad de números
- Permitir especificar si se quiere redondear el resultado
- Añadir la opción de mostrar los pasos intermedios

### 4.2 Nivel Intermedio
**Ejercicio: Generador de Saludos**
- Crear una función que salude a múltiples personas
- Permitir personalizar el mensaje para cada persona
- Añadir opciones como idioma o formalidad

### 4.3 Nivel Avanzado
**Ejercicio: Sistema de Registro**
- Implementar un sistema que registre eventos
- Permitir diferentes tipos de eventos y prioridades
- Añadir opciones de formato y filtrado

## 5. Recursos Adicionales
- **Documentación oficial**: [Python Function Definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- **Tutorial recomendado**: Real Python - [Python Functions](https://realpython.com/defining-your-own-python-function/)
- **Ejercicios adicionales**: [Practice Python](https://www.practicepython.org/)


## 6. Soluciones a los Ejercicios

### 6.1 Solución Nivel Básico: Calculadora Flexible
```python
def calculadora_flexible(*numeros, redondear=False, mostrar_pasos=False):
    """
    Calcula la suma de cualquier cantidad de números con opciones
    de formato

    Args:
        *numeros: Números a sumar
        redondear: Si se debe redondear el resultado
        mostrar_pasos: Si se deben mostrar los pasos intermedios

    Returns:
        float: La suma de los números
    """
    total = 0

    for i, num in enumerate(numeros, 1):
        total += num
        if mostrar_pasos:
            print(f"Paso {i}: {total}")

    if redondear:
        total = round(total)

    return total

# Ejemplos de uso
print("Suma básica:")
print(calculadora_flexible(1, 2, 3))

print("\nCon pasos:")
print(calculadora_flexible(1.5, 2.7, 3.2, mostrar_pasos=True))

print("\nRedondeando:")
print(calculadora_flexible(1.5, 2.7, 3.2, redondear=True))
```

### 6.2 Solución Nivel Intermedio: Generador de Saludos
```python
def generador_saludos(*nombres, idioma="es", formal=False, **personalizado):
    """
    Genera saludos personalizados para múltiples personas

    Args:
        *nombres: Nombres de las personas a saludar
        idioma: Código del idioma (es/en/fr)
        formal: Si el saludo debe ser formal
        **personalizado: Saludos personalizados para personas específicas

    Returns:
        list: Lista de saludos generados
    """
    # Plantillas de saludos según idioma y formalidad
    saludos = {
        "es": {
            "formal": "Estimado/a",
            "informal": "Hola"
        },
        "en": {
            "formal": "Dear",
            "informal": "Hi"
        },
        "fr": {
            "formal": "Cher/Chère",
            "informal": "Salut"
        }
    }

    # Seleccionar el tipo de saludo
    tipo_saludo = "formal" if formal else "informal"
    saludo_base = saludos[idioma][tipo_saludo]

    # Generar saludos
    resultado = []
    for nombre in nombres:
        # Verificar si hay un saludo personalizado
        if nombre in personalizado:
            saludo = f"{personalizado[nombre]} {nombre}!"
        else:
            saludo = f"{saludo_base} {nombre}!"
        resultado.append(saludo)

    return resultado

# Ejemplos de uso
saludos = generador_saludos(
    "Ana", "Juan", "María",
    idioma="es",
    formal=True,
    María="¡Feliz cumpleaños,"
)

for saludo in saludos:
    print(saludo)
```

### 6.3 Solución Nivel Avanzado: Sistema de Registro
```python
def sistema_registro(*eventos, nivel="INFO", formato="simple", **config):
    """
    Sistema de registro de eventos con opciones de configuración

    Args:
        *eventos: Eventos a registrar
        nivel: Nivel de importancia (INFO/WARNING/ERROR)
        formato: Tipo de formato (simple/detallado)
        **config: Configuraciones adicionales

    Returns:
        list: Lista de registros generados
    """
    from datetime import datetime

    def formatear_evento(evento, indice):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if formato == "simple":
            return f"[{nivel}] {timestamp} - {evento}"
        else:
            return {
                "id": indice,
                "timestamp": timestamp,
                "nivel": nivel,
                "mensaje": evento,
                "config": config
            }

    # Procesar cada evento
    registros = []
    for i, evento in enumerate(eventos, 1):
        registro = formatear_evento(evento, i)
        registros.append(registro)

        # Aplicar filtros si existen
        if "filtrar_nivel" in config and nivel != config["filtrar_nivel"]:
            continue

        # Mostrar en consola si está configurado
        if config.get("mostrar_consola", True):
            print(registro)

    return registros

# Ejemplos de uso
registros = sistema_registro(
    "Usuario logueado",
    "Archivo creado",
    "Error en base de datos",
    nivel="WARNING",
    formato="detallado",
    mostrar_consola=True,
    aplicacion="MiApp"
)

# Mostrar todos los registros
print("\nTodos los registros:")
for registro in registros:
    print(registro)
```

## 7. Ejercicios Adicionales para Practicar

### 7.1 Recursividad
1. Implementar la secuencia Fibonacci usando recursividad
2. Crear una función que calcule la potencia de un número recursivamente
3. Desarrollar un buscador de archivos recursivo

### 7.2 Args y Kwargs
1. Crear un formateador de texto que acepte múltiples strings y opciones de formato
2. Implementar una función para crear HTML con tags y atributos variables
3. Desarrollar un sistema de configuración con opciones por defecto y personalizables

### 7.1 Soluciones de Recursividad

#### 1. Secuencia Fibonacci
```python
def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de la secuencia Fibonacci usando recursividad

    Args:
        n: Posición en la secuencia Fibonacci (empezando desde 0)

    Returns:
        int: El número Fibonacci en la posición n
    """
    # Caso base: los dos primeros números de la secuencia
    if n <= 1:
        return n

    # Caso recursivo: cada número es la suma de los dos anteriores
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Función auxiliar para mostrar la secuencia completa
def mostrar_secuencia_fibonacci(n):
    print(f"Secuencia Fibonacci hasta posición {n}:")
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")

# Ejemplo de uso
mostrar_secuencia_fibonacci(10)
```

#### 2. Potencia Recursiva
```python
def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número usando recursividad

    Args:
        base: Número base
        exponente: Exponente (debe ser entero no negativo)

    Returns:
        float: Resultado de base elevado a exponente
    """
    # Validación del exponente
    if not isinstance(exponente, int) or exponente < 0:
        raise ValueError("El exponente debe ser un entero no negativo")

    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1

    # Caso recursivo: multiplicamos la base por sí misma exponente veces
    return base * potencia_recursiva(base, exponente - 1)

# Función para mostrar el proceso
def demostrar_potencia(base, exponente):
    print(f"\nCalculando {base}^{exponente}:")
    resultado = potencia_recursiva(base, exponente)
    print(f"Resultado: {resultado}")
    return resultado

# Ejemplos de uso
demostrar_potencia(2, 4)  # 2^4 = 16
demostrar_potencia(3, 3)  # 3^3 = 27
```

#### 3. Buscador de Archivos Recursivo
```python
import os

def buscar_archivos(directorio, extension=None):
    """
    Busca archivos recursivamente en un directorio y sus subdirectorios

    Args:
        directorio: Ruta del directorio donde buscar
        extension: Extensión de archivo a buscar (opcional)

    Returns:
        list: Lista de archivos encontrados
    """
    archivos_encontrados = []

    try:
        # Listar contenido del directorio
        contenido = os.listdir(directorio)

        for item in contenido:
            ruta_completa = os.path.join(directorio, item)

            # Si es un directorio, búsqueda recursiva
            if os.path.isdir(ruta_completa):
                archivos_encontrados.extend(
                    buscar_archivos(ruta_completa, extension)
                )
            # Si es un archivo, verificar extensión
            elif os.path.isfile(ruta_completa):
                if extension is None or ruta_completa.endswith(extension):
                    archivos_encontrados.append(ruta_completa)

    except PermissionError:
        print(f"Sin acceso a: {directorio}")
    except Exception as e:
        print(f"Error al acceder a {directorio}: {e}")

    return archivos_encontrados

# Función para mostrar resultados de manera organizada
def buscar_y_mostrar(directorio, extension=None):
    print(f"\nBuscando en: {directorio}")
    print(f"Extensión: {extension or 'todas'}")

    archivos = buscar_archivos(directorio, extension)

    print(f"\nArchivos encontrados ({len(archivos)}):")
    for archivo in archivos:
        print(f"- {archivo}")

# Ejemplo de uso
buscar_y_mostrar("./documentos", ".txt")
buscar_y_mostrar("./imagenes", ".jpg")
```

### 7.2 Soluciones de Args y Kwargs

#### 1. Formateador de Texto
```python
def formatear_texto(*textos, mayusculas=False, prefijo="", sufijo="",
                   separador=" ", **estilos):
    """
    Formatea múltiples strings según las opciones especificadas

    Args:
        *textos: Strings a formatear
        mayusculas: Convertir a mayúsculas
        prefijo: Texto a añadir al principio
        sufijo: Texto a añadir al final
        separador: Texto para separar los strings
        **estilos: Opciones adicionales de formato

    Returns:
        str: Texto formateado
    """
    # Procesar cada texto
    textos_procesados = []
    for texto in textos:
        # Aplicar mayúsculas si se especificó
        if mayusculas:
            texto = texto.upper()

        # Aplicar estilos adicionales
        if estilos.get("subrayado"):
            texto = f"_{texto}_"
        if estilos.get("negrita"):
            texto = f"*{texto}*"

        textos_procesados.append(texto)

    # Unir los textos con el separador
    resultado = separador.join(textos_procesados)

    # Añadir prefijo y sufijo
    return f"{prefijo}{resultado}{sufijo}"

# Ejemplos de uso
print(formatear_texto(
    "hola", "mundo", "python",
    mayusculas=True,
    prefijo="¡",
    sufijo="!",
    negrita=True
))

print(formatear_texto(
    "este", "es", "un", "ejemplo",
    separador="-",
    subrayado=True
))
```

#### 2. Generador de HTML
```python
def crear_html(*contenido, tag="div", **atributos):
    """
    Crea elementos HTML con contenido y atributos variables

    Args:
        *contenido: Contenido del elemento HTML
        tag: Tipo de elemento HTML
        **atributos: Atributos HTML (class, id, etc.)

    Returns:
        str: Elemento HTML formateado
    """
    # Procesar atributos
    atributos_str = ""
    for nombre, valor in atributos.items():
        # Convertir guiones bajos a guiones en nombres de atributos
        nombre = nombre.replace("_", "-")
        atributos_str += f' {nombre}="{valor}"'

    # Crear apertura del tag
    html = f"<{tag}{atributos_str}>"

    # Añadir contenido
    if contenido:
        html += "\n"
        for item in contenido:
            html += f"  {item}\n"
        html += f"</{tag}>"
    else:
        html = html[:-1] + "/>"  # Tag autocerrado si no hay contenido

    return html

# Ejemplos de uso
print(crear_html(
    "Título principal",
    tag="h1",
    class_="titulo",
    id="titulo-principal"
))

print(crear_html(
    "Este es un párrafo",
    "Con múltiples líneas",
    tag="p",
    style="color: blue;"
))
```

#### 3. Sistema de Configuración
```python
class ConfiguracionSistema:
    # Valores por defecto
    DEFAULTS = {
        "idioma": "es",
        "tema": "claro",
        "notificaciones": True,
        "tamano_fuente": 12
    }

    def __init__(self, **configuracion):
        """
        Inicializa la configuración con valores por defecto y personalizados

        Args:
            **configuracion: Opciones de configuración personalizadas
        """
        # Combinar valores por defecto con personalizados
        self.config = {**self.DEFAULTS, **configuracion}
        self.historial_cambios = []

    def actualizar(self, **cambios):
        """
        Actualiza la configuración con nuevos valores

        Args:
            **cambios: Nuevos valores de configuración
        """
        for clave, valor in cambios.items():
            if clave in self.config:
                valor_anterior = self.config[clave]
                self.config[clave] = valor
                self.historial_cambios.append({
                    "clave": clave,
                    "anterior": valor_anterior,
                    "nuevo": valor
                })
            else:
                print(f"Advertencia: '{clave}' no es una opción válida")

    def mostrar_configuracion(self):
        """Muestra la configuración actual"""
        print("\nConfiguración actual:")
        for clave, valor in self.config.items():
            print(f"{clave}: {valor}")

    def mostrar_historial(self):
        """Muestra el historial de cambios"""
        if not self.historial_cambios:
            print("\nNo hay cambios registrados")
            return

        print("\nHistorial de cambios:")
        for cambio in self.historial_cambios:
            print(f"- {cambio['clave']}: "
                  f"{cambio['anterior']} → {cambio['nuevo']}")

# Ejemplo de uso
config = ConfiguracionSistema(
    tema="oscuro",
    tamano_fuente=14
)

config.mostrar_configuracion()

config.actualizar(
    idioma="en",
    notificaciones=False
)

config.mostrar_configuracion()
config.mostrar_historial()
```
