# Manejo de Archivos en Python

## 1. Explicación Teórica

### 1.1 Introducción y Fundamentos

El manejo de archivos es una parte fundamental de la programación. Es como tener una biblioteca donde podemos guardar y recuperar información. Python nos proporciona herramientas poderosas y flexibles para trabajar con diferentes tipos de archivos:

1. **Archivos de Texto (.txt)**:
   - Como un cuaderno donde escribimos notas
   - Podemos leer y escribir texto plano
   - Ideal para datos simples y legibles

2. **Archivos CSV (.csv)**:
   - Como una hoja de cálculo simple
   - Organiza datos en filas y columnas
   - Perfecto para datos tabulares

3. **Archivos JSON (.json)**:
   - Como una agenda organizada jerárquicamente
   - Almacena datos estructurados
   - Excelente para intercambio de datos

### 1.2 Modos de Apertura

Cuando trabajamos con archivos, es importante entender los diferentes modos de apertura:

- `'r'`: Modo lectura (por defecto)
- `'w'`: Modo escritura (sobrescribe)
- `'a'`: Modo append (añade al final)
- `'r+'`: Modo lectura y escritura

### 1.3 Contexto y Seguridad

Siempre debemos usar el gestor de contexto `with` para asegurar que los archivos se cierren correctamente:

```python
# Incorrecto
file = open('archivo.txt', 'r')
contenido = file.read()
file.close()

# Correcto
with open('archivo.txt', 'r') as file:
    contenido = file.read()
```

## 2. Archivos de Texto (.txt)

### 2.1 Lectura Básica
```python
def leer_archivo_texto(ruta_archivo):
    """
    Lee un archivo de texto y muestra diferentes formas de acceder al contenido

    Args:
        ruta_archivo: Ruta al archivo de texto
    """
    # Método 1: Leer línea por línea
    print("Leyendo línea por línea:")
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            print(f"Línea: {linea.strip()}")

    # Método 2: Leer todo el contenido
    print("\nLeyendo todo el contenido:")
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(f"Contenido completo:\n{contenido}")

    # Método 3: Leer todas las líneas en una lista
    print("\nLeyendo en lista:")
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas, 1):
            print(f"Línea {i}: {linea.strip()}")
```

### 2.2 Escritura y Modificación
```python
def escribir_archivo_texto(ruta_archivo, contenido, modo='w'):
    """
    Escribe o añade contenido a un archivo de texto

    Args:
        ruta_archivo: Ruta al archivo de texto
        contenido: Texto a escribir
        modo: Modo de escritura ('w' para sobrescribir, 'a' para añadir)
    """
    with open(ruta_archivo, modo, encoding='utf-8') as archivo:
        archivo.write(contenido)

def ejemplo_manejo_texto():
    # Crear un archivo nuevo
    escribir_archivo_texto('notas.txt', 'Primera línea\nSegunda línea\n')

    # Añadir contenido
    escribir_archivo_texto('notas.txt', 'Tercera línea\n', 'a')

    # Leer el resultado
    leer_archivo_texto('notas.txt')
```

### 2.3 Demostración
```python
# demo_texto.py
def demostrar_manejo_texto():
    # 1. Lectura básica
    print("=== Demostración de Lectura ===")
    leer_archivo_texto('ejemplo.txt')

    # 2. Escritura y modificación
    print("\n=== Demostración de Escritura ===")
    # Crear nuevo archivo
    escribir_archivo_texto('notas.txt', 'Primera nota\nSegunda nota\n')
    print("Archivo creado. Contenido inicial:")
    leer_archivo_texto('notas.txt')

    # Añadir contenido
    print("\nAñadiendo contenido...")
    escribir_archivo_texto('notas.txt', 'Tercera nota añadida\n', 'a')
    print("Contenido final:")
    leer_archivo_texto('notas.txt')

if __name__ == "__main__":
    demostrar_manejo_texto()

```
## 3. Archivos CSV

### 3.1 Lectura de CSV
```python
import csv
from typing import List, Dict

def leer_csv_dict(ruta_archivo: str) -> List[Dict]:
    """
    Lee un archivo CSV y retorna una lista de diccionarios

    Args:
        ruta_archivo: Ruta al archivo CSV

    Returns:
        Lista de diccionarios donde cada diccionario representa una fila
    """
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def leer_csv_columnas(ruta_archivo: str, columnas: List[str]) -> None:
    """
    Lee y muestra columnas específicas de un archivo CSV

    Args:
        ruta_archivo: Ruta al archivo CSV
        columnas: Lista de nombres de columnas a mostrar
    """
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            valores = [f"{col}: {fila[col]}" for col in columnas]
            print(", ".join(valores))
```

### 3.2 Escritura y Modificación de CSV
```python
def escribir_csv(ruta_archivo: str, datos: List[Dict],
                modo: str = 'w') -> None:
    """
    Escribe o añade datos a un archivo CSV

    Args:
        ruta_archivo: Ruta al archivo CSV
        datos: Lista de diccionarios con los datos
        modo: Modo de escritura ('w' para nuevo, 'a' para añadir)
    """
    # Si no hay datos, no hacemos nada
    if not datos:
        return

    # Obtenemos los nombres de las columnas del primer diccionario
    campos = list(datos[0].keys())

    with open(ruta_archivo, mode=modo, newline='',
              encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        # Si estamos creando un archivo nuevo, escribimos los encabezados
        if modo == 'w':
            escritor.writeheader()

        # Escribimos los datos
        escritor.writerows(datos)
```
### 3.3 Demostración
```python
# demo_csv.py
def demostrar_manejo_csv():
    print("=== Demostración de Lectura CSV ===")
    # 1. Leer todo el archivo
    datos = leer_csv_dict('empleados.csv')
    print("\nDatos completos:")
    for empleado in datos:
        print(empleado)

    # 2. Leer columnas específicas
    print("\nSolo nombres y salarios:")
    leer_csv_columnas('empleados.csv', ['nombre', 'salario'])

    # 3. Escribir nuevos datos
    nuevos_empleados = [
        {
            'nombre': 'Laura Torres',
            'edad': '33',
            'departamento': 'RRHH',
            'salario': '41000'
        },
        {
            'nombre': 'Pedro Sánchez',
            'edad': '27',
            'departamento': 'IT',
            'salario': '43000'
        }
    ]

    # Crear nuevo archivo
    escribir_csv('nuevos_empleados.csv', nuevos_empleados)
    print("\nNuevo archivo creado. Contenido:")
    datos = leer_csv_dict('nuevos_empleados.csv')
    for empleado in datos:
        print(empleado)

if __name__ == "__main__":
    demostrar_manejo_csv()
```

## 4. Archivos JSON

### 4.1 Lectura de JSON
```python
import json
from typing import Any, Dict, List

def leer_json(ruta_archivo: str) -> Any:
    """
    Lee un archivo JSON y retorna su contenido

    Args:
        ruta_archivo: Ruta al archivo JSON

    Returns:
        Contenido del archivo JSON (puede ser dict, list, etc.)
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def mostrar_json_formateado(datos: Any, nivel: int = 0) -> None:
    """
    Muestra datos JSON de manera formateada y legible

    Args:
        datos: Datos a mostrar
        nivel: Nivel de indentación actual
    """
    indentacion = "  " * nivel

    if isinstance(datos, dict):
        for clave, valor in datos.items():
            print(f"{indentacion}{clave}:")
            mostrar_json_formateado(valor, nivel + 1)
    elif isinstance(datos, list):
        for item in datos:
            mostrar_json_formateado(item, nivel + 1)
    else:
        print(f"{indentacion}{datos}")
```

### 4.2 Escritura y Modificación de JSON
```python
def escribir_json(ruta_archivo: str, datos: Any,
                 indent: int = 4) -> None:
    """
    Escribe datos en un archivo JSON

    Args:
        ruta_archivo: Ruta al archivo JSON
        datos: Datos a escribir
        indent: Número de espacios para indentación
    """
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=indent)

def actualizar_json(ruta_archivo: str,
                   nuevos_datos: Dict) -> None:
    """
    Actualiza un archivo JSON existente

    Args:
        ruta_archivo: Ruta al archivo JSON
        nuevos_datos: Nuevos datos a añadir o actualizar
    """
    # Leer datos existentes
    try:
        datos = leer_json(ruta_archivo)
    except FileNotFoundError:
        datos = {}

    # Actualizar datos
    if isinstance(datos, dict):
        datos.update(nuevos_datos)
    else:
        datos = nuevos_datos

    # Guardar datos actualizados
    escribir_json(ruta_archivo, datos)
```
### 4.3 Demostración

```python
# demo_json.py
def demostrar_manejo_json():
    print("=== Demostración de Lectura JSON ===")
    # 1. Leer y mostrar datos formateados
    datos = leer_json('config.json')
    print("\nDatos formateados:")
    mostrar_json_formateado(datos)

    # 2. Actualizar configuración
    nuevos_ajustes = {
        "app_settings": {
            "debug_mode": False,
            "max_users": 200,
            "allowed_extensions": ["jpg", "png", "pdf", "docx"]
        }
    }

    print("\nActualizando configuración...")
    actualizar_json('config.json', nuevos_ajustes)

    print("\nConfiguración actualizada:")
    datos_actualizados = leer_json('config.json')
    mostrar_json_formateado(datos_actualizados)

    # 3. Crear nuevo archivo JSON
    usuarios = [
        {
            "id": 1,
            "nombre": "Ana",
            "roles": ["admin", "user"]
        },
        {
            "id": 2,
            "nombre": "Juan",
            "roles": ["user"]
        }
    ]

    escribir_json('usuarios.json', usuarios)
    print("\nNuevo archivo de usuarios creado:")
    mostrar_json_formateado(leer_json('usuarios.json'))

if __name__ == "__main__":
    demostrar_manejo_json()

```

## 5. Ejercicios Propuestos - Manipulación de Archivos

### 5.1 Nivel Básico

#### 1. Analizador de Texto
**Objetivo**: Desarrollar un programa que analice el contenido de un archivo de texto y proporcione estadísticas detalladas.

**Requisitos**:
- Contar el número total de palabras
- Identificar las 5 palabras más frecuentes
- Calcular la longitud promedio de las palabras
- Contar el número de párrafos
- Ignorar signos de puntuación y mayúsculas/minúsculas

**Archivo de ejemplo** (`texto_ejemplo.txt`):
```text
Este es un texto de ejemplo para analizar.
Contiene múltiples líneas y palabras repetidas.
Las palabras repetidas nos ayudarán a probar el contador.

Este es otro párrafo del texto.
El análisis debe contar este párrafo como uno nuevo.
```

#### 2. Sistema de Notas Personales
**Objetivo**: Crear un sistema para gestionar notas personales en archivos de texto.

**Requisitos**:
- Crear nuevas notas con título y contenido
- Añadir fecha y hora automáticamente
- Listar todas las notas existentes
- Buscar notas por título o contenido
- Organizar notas en categorías

**Ejemplo de estructura**:
```text
[Título: Reunión de Proyecto]
[Fecha: 2025-02-01 10:30]
[Categoría: Trabajo]
------------------------
Puntos a tratar:
1. Revisar cronograma
2. Asignar tareas
------------------------
```

#### 3. Analizador de Calificaciones
**Objetivo**: Desarrollar un programa que analice calificaciones de estudiantes desde un archivo CSV y genere reportes estadísticos.

**Requisitos**:
- Calcular promedio por estudiante
- Calcular promedio por asignatura
- Identificar calificaciones más altas y más bajas
- Generar reporte de estudiantes en riesgo (promedio < 6)
- Crear gráfico de distribución de notas

**Archivo de ejemplo** (`calificaciones.csv`):
```csv
Estudiante,Matemáticas,Física,Química,Biología
Ana García,8.5,7.8,9.0,8.5
Juan Pérez,6.5,7.0,6.8,7.2
María López,9.0,8.5,8.7,9.0
```

### 5.2 Nivel Intermedio

#### 1. Gestor de Contactos Profesional
**Objetivo**: Implementar un sistema completo de gestión de contactos usando archivos CSV.

**Requisitos**:
- CRUD completo de contactos (Crear, Leer, Actualizar, Eliminar)
- Validación de datos (email, teléfono)
- Búsqueda y filtrado de contactos
- Categorización de contactos
- Exportación de contactos en diferentes formatos
- Manejo de errores y datos duplicados

**Estructura del CSV**:
```csv
id,nombre,email,telefono,categoria,notas
1,Ana García,ana@email.com,+34612345678,Trabajo,Departamento IT
2,Juan Pérez,juan@email.com,+34687654321,Personal,Cumpleaños: 15/03
```

#### 2. Sistema de Registro de Gastos
**Objetivo**: Crear un sistema para registrar y analizar gastos personales usando JSON.

**Requisitos**:
- Registro de gastos con categorías
- Establecer presupuestos por categoría
- Generar reportes mensuales
- Calcular tendencias de gasto
- Exportar informes en diferentes formatos
- Visualización de datos con gráficos

**Estructura JSON**:
```json
{
    "gastos": [
        {
            "fecha": "2025-02-01",
            "categoria": "Alimentación",
            "descripcion": "Supermercado",
            "monto": 75.50,
            "metodo_pago": "Tarjeta"
        }
    ],
    "presupuestos": {
        "Alimentación": 300,
        "Transporte": 150
    }
}
```

#### 3. Integrador de Datos CSV
**Objetivo**: Desarrollar un sistema que combine y analice datos de múltiples archivos CSV.

**Requisitos**:
- Combinar datos basados en una columna común
- Manejar diferentes formatos de fecha
- Resolver conflictos de datos
- Validar integridad de datos
- Generar reporte de inconsistencias
- Exportar resultados consolidados

**Archivos de ejemplo**:
```csv
# ventas_2024_q1.csv
fecha,producto,cantidad,precio
2024-01-15,Laptop,5,999.99

# inventario.csv
producto,stock,proveedor
Laptop,50,TechCorp
```

### 5.3 Nivel Avanzado

#### 1. Mini Base de Datos JSON
**Objetivo**: Implementar un sistema de base de datos simple usando JSON con funcionalidades avanzadas.

**Requisitos**:
- Implementar CRUD completo
- Sistema de índices para búsqueda rápida
- Validación de esquema
- Control de concurrencia básico
- Respaldo automático
- Sistema de consultas simple
- Manejo de relaciones entre entidades

**Ejemplo de implementación**:
```python
class JSONDatabase:
    def __init__(self, file_path, schema=None):
        self.file_path = file_path
        self.schema = schema
        self.indexes = {}
```

#### 2. Conversor Universal de Formatos
**Objetivo**: Crear un sistema flexible para convertir entre diferentes formatos de archivo.

**Requisitos**:
- Conversión bidireccional CSV ↔ JSON
- Preservar tipos de datos
- Manejar datos anidados
- Validar datos durante la conversión
- Configuración personalizable de formato
- Manejo de errores robusto
- Soporte para diferentes encodings

#### 3. Sistema de Logs Avanzado
**Objetivo**: Desarrollar un sistema completo de gestión de logs con características avanzadas.

**Requisitos**:
- Rotación automática por tamaño/tiempo
- Niveles de log (INFO, WARNING, ERROR)
- Compresión de logs antiguos
- Búsqueda y filtrado en logs
- Alertas basadas en patrones
- Estadísticas de errores
- Interfaz de consulta

**Ejemplo de uso**:
```python
logger = AdvancedLogger('app.log',
                       max_size='10MB',
                       backup_count=5,
                       compression=True)
logger.info("Operación completada")
logger.error("Error en proceso", extra={'stack_trace': traceback})
```


## 6. Consideraciones Importantes

### 6.1 Manejo de Errores
```python
def manejo_seguro_archivos(ruta_archivo: str) -> None:
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"No tienes permisos para acceder a {ruta_archivo}")
    except UnicodeDecodeError:
        print(f"Error al decodificar {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado: {e}")
```

### 6.2 Buenas Prácticas
1. Siempre usar `with` para manejar archivos
2. Especificar el encoding (preferiblemente UTF-8)
3. Manejar errores apropiadamente
4. Validar datos antes de escribir
5. Hacer copias de seguridad antes de modificar

### 6.3 Rendimiento y Optimización
1. Usar lectura por líneas para archivos grandes
2. Implementar buffering cuando sea necesario
3. Considerar el uso de bibliotecas especializadas para grandes volúmenes de datos

## 7. Recursos Adicionales
- **Documentación oficial**: [Python File Operations](https://docs.python.org/3/tutorial/inputoutput.html)
- **CSV**: [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- **JSON**: [JSON encoder and decoder](https://docs.python.org/3/library/json.html)

## 8. Solución de Ejercicios

### 8.1 Soluciones Nivel Básico

#### 1. Contador de Palabras
```python
def contar_palabras(ruta_archivo: str) -> dict:
    """
    Lee un archivo de texto y cuenta las palabras,
    proporcionando estadísticas detalladas.

    Args:
        ruta_archivo: Ruta al archivo de texto

    Returns:
        dict: Diccionario con estadísticas de las palabras
    """
    # Inicializamos el contador y estadísticas
    contador_palabras = {}
    estadisticas = {
        'total_palabras': 0,
        'palabras_unicas': 0,
        'palabra_mas_comun': None,
        'frecuencia_maxima': 0
    }

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Limpiamos y dividimos la línea en palabras
                palabras = linea.strip().lower().split()

                for palabra in palabras:
                    # Eliminamos signos de puntuación básicos
                    palabra = palabra.strip('.,!?()[]{}":;')
                    if palabra:
                        contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1

                        # Actualizamos la palabra más común
                        if contador_palabras[palabra] > estadisticas['frecuencia_maxima']:
                            estadisticas['frecuencia_maxima'] = contador_palabras[palabra]
                            estadisticas['palabra_mas_comun'] = palabra

        # Calculamos estadísticas finales
        estadisticas['total_palabras'] = sum(contador_palabras.values())
        estadisticas['palabras_unicas'] = len(contador_palabras)
        estadisticas['contador'] = contador_palabras

        return estadisticas

    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no existe")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Función para mostrar los resultados de manera formateada
def mostrar_estadisticas_palabras(estadisticas: dict) -> None:
    """
    Muestra las estadísticas de palabras de manera formateada
    """
    if not estadisticas:
        return

    print("\n=== Estadísticas de Palabras ===")
    print(f"Total de palabras: {estadisticas['total_palabras']}")
    print(f"Palabras únicas: {estadisticas['palabras_unicas']}")
    print(f"Palabra más común: '{estadisticas['palabra_mas_comun']}' "
          f"({estadisticas['frecuencia_maxima']} veces)")

    print("\nTop 10 palabras más comunes:")
    palabras_ordenadas = sorted(
        estadisticas['contador'].items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    for palabra, frecuencia in palabras_ordenadas:
        print(f"  {palabra}: {frecuencia}")

# Ejemplo de uso
stats = contar_palabras('texto_ejemplo.txt')
mostrar_estadisticas_palabras(stats)
```
