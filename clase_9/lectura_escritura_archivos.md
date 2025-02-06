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
#### 2. Sistema de Notas Simple
```python
from datetime import datetime
from typing import List, Dict

class SistemaNotas:
    def __init__(self, archivo: str):
        self.archivo = archivo

    def agregar_nota(self, titulo: str, contenido: str) -> None:
        """Agrega una nueva nota al archivo"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.archivo, 'a', encoding='utf-8') as f:
            f.write(f"\n=== {titulo} ===\n")
            f.write(f"Fecha: {fecha}\n")
            f.write(f"{contenido}\n")
            f.write("=" * 30 + "\n")

    def leer_notas(self) -> List[Dict]:
        """Lee y retorna todas las notas"""
        notas = []
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                secciones = contenido.split("=" * 30)

                for seccion in secciones:
                    if seccion.strip():
                        # Procesamos cada sección
                        lineas = seccion.strip().split('\n')
                        titulo = lineas[0].strip('= ')
                        fecha = lineas[1].replace('Fecha: ', '')
                        contenido = '\n'.join(lineas[2:])

                        notas.append({
                            'titulo': titulo,
                            'fecha': fecha,
                            'contenido': contenido.strip()
                        })

            return notas

        except FileNotFoundError:
            return []

    def buscar_notas(self, termino: str) -> List[Dict]:
        """Busca notas que contengan el término especificado"""
        notas = self.leer_notas()
        return [
            nota for nota in notas
            if termino.lower() in nota['contenido'].lower() or
               termino.lower() in nota['titulo'].lower()
        ]

    def mostrar_notas(self, notas: List[Dict] = None) -> None:
        """Muestra las notas de manera formateada"""
        if notas is None:
            notas = self.leer_notas()

        if not notas:
            print("No hay notas para mostrar")
            return

        for nota in notas:
            print(f"\n=== {nota['titulo']} ===")
            print(f"Fecha: {nota['fecha']}")
            print(nota['contenido'])
            print("=" * 30)

# Ejemplo de uso
def demostrar_sistema_notas():
    sistema = SistemaNotas('mis_notas.txt')

    # Agregar algunas notas
    sistema.agregar_nota(
        "Reunión de Proyecto",
        "Puntos importantes:\n- Revisar cronograma\n- Asignar tareas\n- Programar siguiente reunión"
    )

    sistema.agregar_nota(
        "Ideas para el fin de semana",
        "1. Ir al parque\n2. Hacer compras\n3. Llamar a Juan"
    )

    # Mostrar todas las notas
    print("=== Todas las notas ===")
    sistema.mostrar_notas()

    # Buscar notas
    print("\n=== Búsqueda: 'reunión' ===")
    notas_encontradas = sistema.buscar_notas('reunión')
    sistema.mostrar_notas(notas_encontradas)

# Ejecutar demostración
demostrar_sistema_notas()
```

#### 3. Calculadora de Promedios CSV
```python
import csv
from typing import Dict, List, Tuple

class CalculadoraCalificaciones:
    def __init__(self, archivo_csv: str):
        self.archivo = archivo_csv

    def leer_calificaciones(self) -> List[Dict]:
        """Lee las calificaciones del archivo CSV"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.archivo}")
            return []

    def calcular_promedio_estudiante(self, calificaciones: Dict[str, str]) -> float:
        """Calcula el promedio de un estudiante"""
        notas = []
        for key, value in calificaciones.items():
            if key != 'Nombre' and key != 'ID':
                try:
                    notas.append(float(value))
                except ValueError:
                    print(f"Advertencia: Calificación inválida para {calificaciones['Nombre']}: {value}")

        return sum(notas) / len(notas) if notas else 0

    def calcular_promedio_materia(self, materia: str) -> Tuple[float, float]:
        """Calcula el promedio y desviación estándar de una materia"""
        calificaciones = []
        estudiantes = self.leer_calificaciones()

        for estudiante in estudiantes:
            try:
                calif = float(estudiante[materia])
                calificaciones.append(calif)
            except (ValueError, KeyError):
                continue

        if not calificaciones:
            return 0, 0

        promedio = sum(calificaciones) / len(calificaciones)

        # Calcular desviación estándar
        varianza = sum((x - promedio) ** 2 for x in calificaciones) / len(calificaciones)
        desviacion = varianza ** 0.5

        return promedio, desviacion

    def generar_reporte(self) -> None:
        """Genera un reporte completo de calificaciones"""
        estudiantes = self.leer_calificaciones()
        if not estudiantes:
            return

        materias = [key for key in estudiantes[0].keys()
                   if key not in ['Nombre', 'ID']]

        print("\n=== Reporte de Calificaciones ===")

        # Promedios por estudiante
        print("\nPromedios por Estudiante:")
        for estudiante in estudiantes:
            promedio = self.calcular_promedio_estudiante(estudiante)
            print(f"{estudiante['Nombre']}: {promedio:.2f}")

        # Promedios por materia
        print("\nEstadísticas por Materia:")
        for materia in materias:
            promedio, desviacion = self.calcular_promedio_materia(materia)
            print(f"\n{materia}:")
            print(f"  Promedio: {promedio:.2f}")
            print(f"  Desviación Estándar: {desviacion:.2f}")

        # Encontrar mejores estudiantes
        estudiantes_ordenados = sorted(
            estudiantes,
            key=lambda x: self.calcular_promedio_estudiante(x),
            reverse=True
        )

        print("\nTop 3 Estudiantes:")
        for i, estudiante in enumerate(estudiantes_ordenados[:3], 1):
            promedio = self.calcular_promedio_estudiante(estudiante)
            print(f"{i}. {estudiante['Nombre']}: {promedio:.2f}")

# Ejemplo de uso
def demostrar_calculadora():
    calc = CalculadoraCalificaciones('calificaciones.csv')
    calc.generar_reporte()

# Ejecutar demostración
demostrar_calculadora()
```

### 8.2 Soluciones Nivel Intermedio

#### 1. Gestor de Contactos CSV
```python
from typing import List, Dict
import csv
from datetime import datetime

class GestorContactos:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.campos = ['nombre', 'telefono', 'email',
                      'direccion', 'ultima_actualizacion']
        self._inicializar_archivo()

    def _inicializar_archivo(self) -> None:
        """
        Inicializa el archivo CSV si no existe.
        Crea la estructura básica con los campos necesarios.
        """
        try:
            with open(self.archivo, 'x', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
        except FileExistsError:
            pass  # El archivo ya existe, no necesitamos inicializarlo

    def agregar_contacto(self, contacto: Dict) -> bool:
        """
        Agrega un nuevo contacto al sistema.
        Valida los datos antes de agregarlos.

        Args:
            contacto: Diccionario con los datos del contacto

        Returns:
            bool: True si se agregó correctamente, False si hubo error
        """
        # Validar campos requeridos
        if not contacto.get('nombre') or not contacto.get('telefono'):
            print("Error: Nombre y teléfono son campos obligatorios")
            return False

        # Añadir fecha de actualización
        contacto['ultima_actualizacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.archivo, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writerow(contacto)
            return True
        except Exception as e:
            print(f"Error al agregar contacto: {e}")
            return False

    def buscar_contacto(self, termino: str) -> List[Dict]:
        """
        Busca contactos que coincidan con el término proporcionado.
        La búsqueda es case-insensitive y parcial.

        Args:
            termino: Término a buscar

        Returns:
            Lista de contactos que coinciden con la búsqueda
        """
        resultados = []
        termino = termino.lower()

        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for contacto in reader:
                    # Buscar en todos los campos
                    if any(termino in valor.lower()
                          for valor in contacto.values()):
                        resultados.append(contacto)
        except Exception as e:
            print(f"Error al buscar contactos: {e}")

        return resultados

    def actualizar_contacto(self, nombre: str, nuevos_datos: Dict) -> bool:
        """
        Actualiza los datos de un contacto existente.

        Args:
            nombre: Nombre del contacto a actualizar
            nuevos_datos: Nuevos datos para el contacto

        Returns:
            bool: True si se actualizó correctamente
        """
        contactos_actualizados = []
        encontrado = False

        try:
            # Leer todos los contactos
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for contacto in reader:
                    if contacto['nombre'] == nombre:
                        # Actualizar datos manteniendo los campos no modificados
                        contacto.update(nuevos_datos)
                        contacto['ultima_actualizacion'] = \
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        encontrado = True
                    contactos_actualizados.append(contacto)

            if not encontrado:
                print(f"No se encontró el contacto: {nombre}")
                return False

            # Escribir todos los contactos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
                writer.writerows(contactos_actualizados)

            return True

        except Exception as e:
            print(f"Error al actualizar contacto: {e}")
            return False

    def eliminar_contacto(self, nombre: str) -> bool:
        """
        Elimina un contacto del sistema.

        Args:
            nombre: Nombre del contacto a eliminar

        Returns:
            bool: True si se eliminó correctamente
        """
        contactos_restantes = []
        encontrado = False

        try:
            # Leer y filtrar contactos
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for contacto in reader:
                    if contacto['nombre'] != nombre:
                        contactos_restantes.append(contacto)
                    else:
                        encontrado = True

            if not encontrado:
                print(f"No se encontró el contacto: {nombre}")
                return False

            # Escribir los contactos restantes
            with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
                writer.writerows(contactos_restantes)

            return True

        except Exception as e:
            print(f"Error al eliminar contacto: {e}")
            return False

# Ejemplo de uso del gestor de contactos
def demostrar_gestor_contactos():
    gestor = GestorContactos('contactos.csv')

    # Agregar algunos contactos
    gestor.agregar_contacto({
        'nombre': 'Ana García',
        'telefono': '123-456-789',
        'email': 'ana@email.com',
        'direccion': 'Calle Principal 123'
    })

    gestor.agregar_contacto({
        'nombre': 'Juan Pérez',
        'telefono': '987-654-321',
        'email': 'juan@email.com',
        'direccion': 'Avenida Central 456'
    })

    # Buscar contactos
    print("\nBúsqueda por 'ana':")
    resultados = gestor.buscar_contacto('ana')
    for contacto in resultados:
        print(contacto)

    # Actualizar un contacto
    gestor.actualizar_contacto('Ana García', {
        'telefono': '111-222-333',
        'email': 'ana.garcia@email.com'
    })

    # Eliminar un contacto
    gestor.eliminar_contacto('Juan Pérez')

# Ejecutar demostración
if __name__ == "__main__":
    demostrar_gestor_contactos()
```

#### 2. Sistema de Registro de Gastos con JSON
```python
import json
from datetime import datetime
from typing import List, Dict, Optional
import os

class RegistroGastos:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.categorias_default = [
            "Alimentación", "Transporte", "Vivienda",
            "Entretenimiento", "Salud", "Otros"
        ]
        self._inicializar_archivo()

    def _inicializar_archivo(self) -> None:
        """
        Inicializa el archivo JSON si no existe con una estructura básica
        """
        if not os.path.exists(self.archivo):
            estructura_inicial = {
                "categorias": self.categorias_default,
                "gastos": [],
                "presupuestos": {},
                "ultima_actualizacion": datetime.now().isoformat()
            }
            self._guardar_datos(estructura_inicial)

    def _cargar_datos(self) -> Dict:
        """
        Carga los datos del archivo JSON

        Returns:
            Dict: Datos del registro de gastos
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"categorias": [], "gastos": [], "presupuestos": {}}

    def _guardar_datos(self, datos: Dict) -> None:
        """
        Guarda los datos en el archivo JSON

        Args:
            datos: Diccionario con los datos a guardar
        """
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def agregar_gasto(self, concepto: str, monto: float,
                     categoria: str, fecha: Optional[str] = None) -> bool:
        """
        Agrega un nuevo gasto al registro

        Args:
            concepto: Descripción del gasto
            monto: Cantidad gastada
            categoria: Categoría del gasto
            fecha: Fecha del gasto (opcional, por defecto fecha actual)

        Returns:
            bool: True si se agregó correctamente
        """
        datos = self._cargar_datos()

        # Validar categoría
        if categoria not in datos["categorias"]:
            print(f"Categoría inválida. Categorías disponibles: {datos['categorias']}")
            return False

        # Crear nuevo gasto
        nuevo_gasto = {
            "id": len(datos["gastos"]) + 1,
            "concepto": concepto,
            "monto": float(monto),
            "categoria": categoria,
            "fecha": fecha or datetime.now().isoformat(),
            "timestamp": datetime.now().isoformat()
        }

        datos["gastos"].append(nuevo_gasto)
        datos["ultima_actualizacion"] = datetime.now().isoformat()

        self._guardar_datos(datos)
        return True

    def establecer_presupuesto(self, categoria: str, monto: float) -> bool:
        """
        Establece un presupuesto para una categoría

        Args:
            categoria: Categoría para el presupuesto
            monto: Monto del presupuesto

        Returns:
            bool: True si se estableció correctamente
        """
        datos = self._cargar_datos()

        if categoria not in datos["categorias"]:
            print(f"Categoría inválida. Categorías disponibles: {datos['categorias']}")
            return False

        datos["presupuestos"][categoria] = float(monto)
        self._guardar_datos(datos)
        return True

    def obtener_gastos_por_categoria(self, categoria: Optional[str] = None) -> Dict:
        """
        Obtiene un resumen de gastos por categoría

        Args:
            categoria: Categoría específica (opcional)

        Returns:
            Dict: Resumen de gastos
        """
        datos = self._cargar_datos()
        resumen = {}

        for gasto in datos["gastos"]:
            cat = gasto["categoria"]
            if categoria and cat != categoria:
                continue

            if cat not in resumen:
                resumen[cat] = {
                    "total": 0,
                    "gastos": [],
                    "presupuesto": datos["presupuestos"].get(cat, 0)
                }

            resumen[cat]["total"] += gasto["monto"]
            resumen[cat]["gastos"].append(gasto)

        return resumen

    def generar_reporte(self) -> None:
        """
        Genera un reporte detallado de gastos
        """
        datos = self._cargar_datos()
        resumen = self.obtener_gastos_por_categoria()

        print("\n=== REPORTE DE GASTOS ===")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 30)

        total_general = 0
        for categoria, info in resumen.items():
            total = info["total"]
            total_general += total
            presupuesto = info["presupuesto"]

            print(f"\nCategoría: {categoria}")
            print(f"Total gastado: ${total:.2f}")
            print(f"Presupuesto: ${presupuesto:.2f}")

            if presupuesto > 0:
                porcentaje = (total / presupuesto) * 100
                print(f"Porcentaje del presupuesto: {porcentaje:.1f}%")

            print("\nGastos detallados:")
            for gasto in info["gastos"]:
                fecha = datetime.fromisoformat(gasto["fecha"]).strftime("%Y-%m-%d")
                print(f"- {fecha}: {gasto['concepto']} (${gasto['monto']:.2f})")

        print("\n" + "=" * 30)
        print(f"TOTAL GENERAL: ${total_general:.2f}")

# Ejemplo de uso
def demostrar_registro_gastos():
    registro = RegistroGastos('gastos.json')

    # Establecer algunos presupuestos
    registro.establecer_presupuesto("Alimentación", 500)
    registro.establecer_presupuesto("Transporte", 200)

    # Agregar algunos gastos
    registro.agregar_gasto("Supermercado", 150.50, "Alimentación")
    registro.agregar_gasto("Gasolina", 45.00, "Transporte")
    registro.agregar_gasto("Restaurante", 35.75, "Alimentación")

    # Generar reporte
    registro.generar_reporte()

# Ejecutar demostración
if __name__ == "__main__":
    demostrar_registro_gastos()
```

Para usar este sistema, necesitarás un archivo `gastos.json` inicial (aunque el sistema lo creará si no existe):

```json
{
    "categorias": [
        "Alimentación",
        "Transporte",
        "Vivienda",
        "Entretenimiento",
        "Salud",
        "Otros"
    ],
    "gastos": [],
    "presupuestos": {},
    "ultima_actualizacion": "2025-02-01T10:00:00"
}
```

#### 3. Combinador de Datos CSV

```python
import csv
from datetime import datetime
from typing import List, Dict, Any
import os
from collections import defaultdict

class CombinadorCSV:
    """
    Clase para combinar y analizar datos de múltiples archivos CSV.
    Incluye funcionalidades para procesamiento, análisis y generación de reportes.
    """

    def __init__(self, directorio: str, patron: str = "ventas_*.csv"):
        """
        Inicializa el combinador de CSV.

        Args:
            directorio: Ruta al directorio con los archivos CSV
            patron: Patrón para identificar los archivos a combinar
        """
        self.directorio = directorio
        self.patron = patron
        self.archivos = []
        self.datos_combinados = []
        self._encontrar_archivos()

    def _encontrar_archivos(self) -> None:
        """
        Busca los archivos CSV que coincidan con el patrón especificado.
        """
        import glob
        ruta_patron = os.path.join(self.directorio, self.patron)
        self.archivos = glob.glob(ruta_patron)
        print(f"Archivos encontrados: {len(self.archivos)}")
        for archivo in self.archivos:
            print(f"- {os.path.basename(archivo)}")

    def _validar_fila(self, fila: Dict[str, Any],
                     campos_requeridos: List[str]) -> bool:
        """
        Valida que una fila contenga todos los campos requeridos.

        Args:
            fila: Diccionario con los datos de la fila
            campos_requeridos: Lista de campos que deben estar presentes

        Returns:
            bool: True si la fila es válida
        """
        return all(campo in fila and fila[campo] for campo in campos_requeridos)

    def combinar_archivos(self, campos_requeridos: List[str] = None) -> None:
        """
        Combina los datos de todos los archivos CSV encontrados.

        Args:
            campos_requeridos: Lista de campos que deben estar presentes
        """
        self.datos_combinados = []
        filas_invalidas = 0

        for archivo in self.archivos:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for fila in reader:
                        # Validar campos requeridos si se especificaron
                        if campos_requeridos and not self._validar_fila(fila,
                                                                       campos_requeridos):
                            filas_invalidas += 1
                            continue

                        # Agregar metadatos del archivo
                        fila['archivo_origen'] = os.path.basename(archivo)
                        self.datos_combinados.append(fila)

            except Exception as e:
                print(f"Error al procesar {archivo}: {e}")

        print(f"\nResumen de combinación:")
        print(f"- Total de filas procesadas: {len(self.datos_combinados)}")
        print(f"- Filas inválidas ignoradas: {filas_invalidas}")

    def analizar_datos(self) -> Dict:
        """
        Realiza un análisis básico de los datos combinados.

        Returns:
            Dict: Diccionario con estadísticas y análisis
        """
        if not self.datos_combinados:
            return {}

        analisis = {
            "total_registros": len(self.datos_combinados),
            "por_producto": defaultdict(lambda: {
                "cantidad_total": 0,
                "ventas_totales": 0.0,
                "precio_promedio": 0.0
            }),
            "por_mes": defaultdict(lambda: {
                "cantidad_total": 0,
                "ventas_totales": 0.0
            })
        }

        for registro in self.datos_combinados:
            try:
                # Procesar datos numéricos
                cantidad = int(registro['cantidad'])
                precio = float(registro['precio_unitario'])
                total = cantidad * precio

                # Actualizar estadísticas por producto
                producto = registro['producto']
                analisis["por_producto"][producto]["cantidad_total"] += cantidad
                analisis["por_producto"][producto]["ventas_totales"] += total

                # Calcular mes de la venta
                fecha = datetime.strptime(registro['fecha'], '%Y-%m-%d')
                mes = fecha.strftime('%Y-%m')

                # Actualizar estadísticas por mes
                analisis["por_mes"][mes]["cantidad_total"] += cantidad
                analisis["por_mes"][mes]["ventas_totales"] += total

            except Exception as e:
                print(f"Error al procesar registro: {e}")
                continue

        # Calcular precios promedio por producto
        for producto, stats in analisis["por_producto"].items():
            if stats["cantidad_total"] > 0:
                stats["precio_promedio"] = (
                    stats["ventas_totales"] / stats["cantidad_total"]
                )

        return analisis

    def generar_reporte(self, ruta_salida: str) -> None:
        """
        Genera un reporte detallado en formato CSV.

        Args:
            ruta_salida: Ruta donde guardar el reporte
        """
        analisis = self.analizar_datos()

        with open(ruta_salida, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Escribir encabezado
            writer.writerow(['REPORTE DE VENTAS COMBINADO'])
            writer.writerow([])

            # Resumen por producto
            writer.writerow(['RESUMEN POR PRODUCTO'])
            writer.writerow(['Producto', 'Cantidad Total', 'Ventas Totales',
                           'Precio Promedio'])

            for producto, stats in analisis["por_producto"].items():
                writer.writerow([
                    producto,
                    stats["cantidad_total"],
                    f"${stats['ventas_totales']:.2f}",
                    f"${stats['precio_promedio']:.2f}"
                ])

            writer.writerow([])

            # Resumen por mes
            writer.writerow(['RESUMEN POR MES'])
            writer.writerow(['Mes', 'Cantidad Total', 'Ventas Totales'])

            for mes, stats in sorted(analisis["por_mes"].items()):
                writer.writerow([
                    mes,
                    stats["cantidad_total"],
                    f"${stats['ventas_totales']:.2f}"
                ])

# Ejemplo de uso
def demostrar_combinador():
    """
    Demuestra el uso del combinador de CSV con archivos de ejemplo.
    """
    combinador = CombinadorCSV("./datos")

    # Combinar archivos especificando campos requeridos
    campos_requeridos = ['fecha', 'producto', 'cantidad', 'precio_unitario']
    combinador.combinar_archivos(campos_requeridos)

    # Generar reporte
    combinador.generar_reporte('reporte_ventas_combinado.csv')

if __name__ == "__main__":
    demostrar_combinador()
```

Este código crea un sistema completo para combinar y analizar datos de múltiples archivos CSV. Al ejecutarlo con los archivos de ejemplo, generará un reporte detallado que incluirá:
- Resumen de ventas por producto
- Análisis temporal de ventas
- Estadísticas agregadas

### 8.3 Soluciones Nivel Avanzado

#### 1. Sistema de Base de Datos Simple con JSON
```python
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import defaultdict

class SimpleDB:
    """
    Una implementación simple de base de datos usando JSON como almacenamiento.
    Incluye características básicas de una base de datos como:
    - CRUD (Crear, Leer, Actualizar, Eliminar)
    - Índices para búsqueda rápida
    - Validación de esquemas
    - Control de versiones básico
    """

    def __init__(self, nombre_db: str, esquema: Dict = None):
        """
        Inicializa la base de datos.

        Args:
            nombre_db: Nombre de la base de datos (se usará como nombre de archivo)
            esquema: Diccionario definiendo la estructura de los datos
        """
        self.nombre_db = f"{nombre_db}.json"
        self.esquema = esquema or {}
        self.indices = {}
        self._inicializar_db()

    def _inicializar_db(self) -> None:
        """
        Inicializa la estructura de la base de datos si no existe.
        Crea los archivos necesarios y los índices iniciales.
        """
        if not os.path.exists(self.nombre_db):
            estructura_inicial = {
                "metadata": {
                    "version": "1.0",
                    "fecha_creacion": datetime.now().isoformat(),
                    "ultima_actualizacion": datetime.now().isoformat(),
                    "num_registros": 0
                },
                "esquema": self.esquema,
                "datos": [],
                "indices": {},
                "historial_cambios": []
            }
            self._guardar_db(estructura_inicial)
        else:
            # Verificar y actualizar esquema si es necesario
            db = self._cargar_db()
            if self.esquema and db["esquema"] != self.esquema:
                self._migrar_esquema(db)

    def _cargar_db(self) -> Dict:
        """
        Carga los datos de la base de datos desde el archivo.

        Returns:
            Dict: Contenido de la base de datos
        """
        try:
            with open(self.nombre_db, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Base de datos no encontrada")

    def _guardar_db(self, datos: Dict) -> None:
        """
        Guarda los datos en el archivo de la base de datos.
        Actualiza la metadata automáticamente.

        Args:
            datos: Diccionario con los datos a guardar
        """
        # Actualizar metadata
        datos["metadata"]["ultima_actualizacion"] = datetime.now().isoformat()
        datos["metadata"]["num_registros"] = len(datos["datos"])

        with open(self.nombre_db, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def _validar_registro(self, registro: Dict) -> bool:
        """
        Valida un registro contra el esquema definido.

        Args:
            registro: Registro a validar

        Returns:
            bool: True si el registro es válido
        """
        if not self.esquema:
            return True

        for campo, tipo in self.esquema.items():
            if campo not in registro:
                return False
            if not isinstance(registro[campo], eval(tipo)):
                return False
        return True

    def _reconstruir_indices(self, db: Dict) -> None:
        """
        Reconstruye los índices de la base de datos.

        Args:
            db: Diccionario con los datos de la base de datos
        """
        indices = defaultdict(dict)
        for i, registro in enumerate(db["datos"]):
            for campo in self.esquema.keys():
                if campo in registro:
                    valor = registro[campo]
                    if isinstance(valor, (str, int, float)):
                        indices[campo][valor] = i

        db["indices"] = indices

    def insertar(self, registro: Dict) -> bool:
        """
        Inserta un nuevo registro en la base de datos.

        Args:
            registro: Registro a insertar

        Returns:
            bool: True si se insertó correctamente
        """
        if not self._validar_registro(registro):
            raise ValueError("Registro inválido según el esquema")

        db = self._cargar_db()

        # Agregar metadata al registro
        registro["_id"] = len(db["datos"])
        registro["_creado"] = datetime.now().isoformat()
        registro["_modificado"] = registro["_creado"]

        # Insertar registro
        db["datos"].append(registro)

        # Actualizar índices
        self._reconstruir_indices(db)

        # Registrar cambio
        db["historial_cambios"].append({
            "tipo": "insercion",
            "registro_id": registro["_id"],
            "fecha": datetime.now().isoformat()
        })

        self._guardar_db(db)
        return True

    def buscar(self, criterios: Dict) -> List[Dict]:
        """
        Busca registros que coincidan con los criterios especificados.

        Args:
            criterios: Diccionario con los criterios de búsqueda

        Returns:
            List[Dict]: Lista de registros que coinciden
        """
        db = self._cargar_db()
        resultados = []

        # Intentar usar índices para búsqueda rápida
        if len(criterios) == 1 and list(criterios.keys())[0] in db["indices"]:
            campo = list(criterios.keys())[0]
            valor = criterios[campo]
            if valor in db["indices"][campo]:
                indice = db["indices"][campo][valor]
                return [db["datos"][indice]]

        # Búsqueda completa si no se pueden usar índices
        for registro in db["datos"]:
            coincide = True
            for campo, valor in criterios.items():
                if campo not in registro or registro[campo] != valor:
                    coincide = False
                    break
            if coincide:
                resultados.append(registro)

        return resultados

    def actualizar(self, criterios: Dict, nuevos_valores: Dict) -> int:
        """
        Actualiza registros que coincidan con los criterios.

        Args:
            criterios: Criterios para seleccionar registros
            nuevos_valores: Nuevos valores a establecer

        Returns:
            int: Número de registros actualizados
        """
        db = self._cargar_db()
        actualizados = 0

        for registro in db["datos"]:
            coincide = True
            for campo, valor in criterios.items():
                if campo not in registro or registro[campo] != valor:
                    coincide = False
                    break

            if coincide:
                for campo, valor in nuevos_valores.items():
                    if campo in self.esquema:
                        registro[campo] = valor
                registro["_modificado"] = datetime.now().isoformat()
                actualizados += 1

        if actualizados > 0:
            self._reconstruir_indices(db)
            db["historial_cambios"].append({
                "tipo": "actualizacion",
                "criterios": criterios,
                "nuevos_valores": nuevos_valores,
                "registros_afectados": actualizados,
                "fecha": datetime.now().isoformat()
            })
            self._guardar_db(db)

        return actualizados

    def eliminar(self, criterios: Dict) -> int:
        """
        Elimina registros que coincidan con los criterios.

        Args:
            criterios: Criterios para seleccionar registros a eliminar

        Returns:
            int: Número de registros eliminados
        """
        db = self._cargar_db()
        registros_originales = db["datos"].copy()
        nuevos_registros = []
        eliminados = 0

        for registro in registros_originales:
            coincide = True
            for campo, valor in criterios.items():
                if campo not in registro or registro[campo] != valor:
                    coincide = False
                    break

            if not coincide:
                nuevos_registros.append(registro)
            else:
                eliminados += 1

        if eliminados > 0:
            db["datos"] = nuevos_registros
            self._reconstruir_indices(db)
            db["historial_cambios"].append({
                "tipo": "eliminacion",
                "criterios": criterios,
                "registros_afectados": eliminados,
                "fecha": datetime.now().isoformat()
            })
            self._guardar_db(db)

        return eliminados

# Ejemplo de uso
def demostrar_base_datos():
    """
    Demuestra el uso del sistema de base de datos simple.
    """
    # Definir esquema
    esquema = {
        "nombre": "str",
        "edad": "int",
        "correo": "str",
        "activo": "bool"
    }

    # Crear base de datos
    db = SimpleDB("usuarios", esquema)

    # Insertar algunos registros
    db.insertar({
        "nombre": "Ana García",
        "edad": 28,
        "correo": "ana@email.com",
        "activo": True
    })

    db.insertar({
        "nombre": "Juan Pérez",
        "edad": 35,
        "correo": "juan@email.com",
        "activo": True
    })

    # Realizar búsquedas
    usuarios_activos = db.buscar({"activo": True})
    print("\nUsuarios activos:")
    for usuario in usuarios_activos:
        print(f"- {usuario['nombre']} ({usuario['correo']})")

    # Actualizar registros
    actualizados = db.actualizar(
        {"nombre": "Ana García"},
        {"edad": 29}
    )
    print(f"\nRegistros actualizados: {actualizados}")

    # Eliminar registros
    eliminados = db.eliminar({"activo": False})
    print(f"\nRegistros eliminados: {eliminados}")

if __name__ == "__main__":
    demostrar_base_datos()
```
