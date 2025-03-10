# 🛡️ Manejo de Excepciones en Python

## Fundamentos de Excepciones

### ¿Qué es una Excepción?
Una excepción es una interrupción en el flujo normal de un programa cuando ocurre un error. Imagina que estás siguiendo una receta de cocina: una excepción sería como encontrarte con que te falta un ingrediente esencial. En programación, necesitamos manejar estas situaciones de manera elegante.

### ¿Por qué son Importantes?
El manejo de excepciones nos permite:
1. Prevenir que nuestro programa se detenga abruptamente
2. Proporcionar mensajes de error útiles
3. Implementar planes alternativos cuando algo falla
4. Mantener un registro de errores para depuración

## Anatomía del Manejo de Excepciones

### Estructura Básica
```python
try:
    # Código que podría fallar
    edad = int(input("¿Cuál es tu edad? "))

except ValueError:
    # Plan B: qué hacer si algo sale mal
    print("Por favor, ingresa un número válido")

else:
    # Código que se ejecuta si todo sale bien
    print(f"Tienes {edad} años")

finally:
    # Código que se ejecuta siempre
    print("Gracias por usar el programa")
```

### Explicación de cada Bloque

#### El Bloque try
Es como un laboratorio de pruebas donde colocamos el código que podría generar errores. Python vigilará este código especialmente.

#### El Bloque except
Es nuestro plan de contingencia. Aquí especificamos qué hacer cuando ocurre un error específico.

#### El Bloque else
Este bloque es como un premio por la ejecución exitosa. Solo se ejecuta si no hubo excepciones.

#### El Bloque finally
Es nuestro código de limpieza. Se ejecutará sin importar qué suceda, como limpiar la cocina después de cocinar.

## Jerarquía de Excepciones

Las excepciones en Python están organizadas como una familia, con BaseException como el ancestro común.

### Estructura Jerárquica Principal
```
BaseException
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    └── [Otras Excepciones]
```

## Excepciones Comunes y su Manejo

### Errores Matemáticos
```python
def division_segura():
    try:
        numerador = float(input("Ingresa el numerador: "))
        denominador = float(input("Ingresa el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado es: {resultado}")
    except ZeroDivisionError:
        print("¡No puedes dividir entre cero!")
    except ValueError:
        print("Por favor, ingresa solo números")
```

### Errores de Acceso
```python
def acceder_lista():
    mi_lista = [1, 2, 3]
    try:
        indice = int(input("¿Qué posición quieres ver? "))
        valor = mi_lista[indice]
        print(f"El valor es: {valor}")
    except IndexError:
        print(f"Solo hay {len(mi_lista)} elementos (0-{len(mi_lista)-1})")
```

## 🎯 Estrategias Avanzadas

### Captura de Múltiples Excepciones
Podemos manejar diferentes tipos de errores en el mismo bloque try:

```python
def operacion_bancaria():
    try:
        saldo = float(input("Ingresa tu saldo: "))
        retiro = float(input("Cantidad a retirar: "))

        if retiro > saldo:
            raise ValueError("Fondos insuficientes")

        nuevo_saldo = saldo - retiro
        print(f"Nuevo saldo: ${nuevo_saldo:.2f}")

    except ValueError as error:
        if str(error) == "Fondos insuficientes":
            print("❌ Error: No tienes suficiente saldo")
        else:
            print("❌ Error: Por favor, ingresa cantidades válidas")
    except Exception as error:
        print(f"❌ Error inesperado: {error}")
```

### Creación de Excepciones Personalizadas
Podemos crear nuestras propias excepciones para casos específicos:

```python
class EdadInvalidaError(Exception):
    """Excepción para edades fuera de rango"""
    pass

def verificar_edad(edad):
    try:
        edad = int(edad)
        if edad < 0 or edad > 150:
            raise EdadInvalidaError("La edad debe estar entre 0 y 150 años")
        return True
    except EdadInvalidaError as e:
        print(f"Error de validación: {e}")
        return False
    except ValueError:
        print("Error: Debes ingresar un número")
        return False
```

## 📚 Casos de Uso del Mundo Real

### 1. Validación de Formularios
```python
def validar_registro():
    try:
        # Recopilación de datos
        email = input("Email: ").strip()
        edad = int(input("Edad: "))
        contraseña = input("Contraseña: ")

        # Validaciones
        if '@' not in email or '.' not in email:
            raise ValueError("Email inválido")

        if edad < 18:
            raise ValueError("Debes ser mayor de edad")

        if len(contraseña) < 8:
            raise ValueError("La contraseña es muy corta")

        print("✅ Registro exitoso")

    except ValueError as e:
        print(f"❌ Error de validación: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
```

### 2. Manejo de Archivos Seguro
```python
def leer_archivo_seguro(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido

    except FileNotFoundError:
        print(f"❌ El archivo '{nombre_archivo}' no existe")
        return None
    except PermissionError:
        print("❌ No tienes permiso para leer este archivo")
        return None
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")
        return None
```

## 💡 Mejores Prácticas Detalladas

### 1. Especificidad en las Excepciones
```python
# ❌ Mal: Demasiado general
try:
    hacer_algo()
except Exception:
    print("Error")

# ✅ Bien: Excepciones específicas
try:
    hacer_algo()
except ValueError:
    print("Error: Valor inválido")
except TypeError:
    print("Error: Tipo incorrecto")
```

### 2. Manejo Contextual
```python
# ❌ Mal: Demasiado código en el try
try:
    # Muchas líneas de código...
    pass
except Exception:
    pass

# ✅ Bien: Try específico
try:
    resultado = numero / divisor
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

## 📝 Consejos Finales
1. Siempre documentar el propósito de cada try-except
2. Mantener los bloques try lo más pequeños posible
3. No silenciar excepciones sin un buen motivo
4. Usar finally para limpieza de recursos
5. Crear mensajes de error informativos y útiles


## Ejercicio 1: Conversor de Temperatura

### Enunciado 📝
Crea un programa que convierta temperaturas de Celsius a Fahrenheit. Debe:
* Pedir al usuario una temperatura en Celsius
* Convertirla a Fahrenheit usando la fórmula: °F = (°C × 9/5) + 32
* Manejar posibles errores de entrada
* Usar todos los bloques (try/except/else/finally)
* Permitir al usuario convertir múltiples temperaturas

### Ejemplo de Ejecución
```
=== CONVERSOR DE TEMPERATURA ===
Ingresa la temperatura en Celsius: 25
✅ 25°C = 77.0°F
🔚 Conversión finalizada

Ingresa la temperatura en Celsius: abc
❌ Error: Debes ingresar un número válido
🔚 Conversión finalizada

Ingresa la temperatura en Celsius: -273.16
❌ Error: La temperatura está por debajo del cero absoluto (-273.15°C)
🔚 Conversión finalizada
```

## Ejercicio 2: Registro de Usuario

### Enunciado 📝
Desarrolla un sistema de registro que:
* Solicite nombre, edad y correo electrónico
* Valide que el nombre no esté vacío
* Compruebe que la edad sea un número entre 0 y 120
* Verifique que el correo contenga '@' y '.'
* Maneje todos los posibles errores
* Guarde los datos si todo es correcto

### Ejemplo de Ejecución
```
=== SISTEMA DE REGISTRO ===
Nombre:
❌ Error: El nombre no puede estar vacío

Nombre: Juan
Edad: abc
❌ Error: La edad debe ser un número

Nombre: Juan
Edad: 25
Email: juangmail
❌ Error: Email inválido. Debe contener '@' y '.'

Nombre: Juan
Edad: 25
Email: juan@gmail.com
✅ Usuario registrado correctamente:
- Nombre: Juan
- Edad: 25
- Email: juan@gmail.com
```

## Reto Final: Super Calculadora

### Enunciado 📝
Crea una calculadora avanzada que:
1. Muestre un menú con operaciones:
   * Suma (+)
   * Resta (-)
   * Multiplicación (*)
   * División (/)
   * Potencia (**)
   * Raíz cuadrada (√)
2. Maneje todos los posibles errores:
   * Entradas no numéricas
   * División por cero
   * Raíces de números negativos
   * Operadores inválidos
3. Muestre resultados con 2 decimales
4. Permita continuar o salir después de cada operación
5. Mantenga un historial de operaciones

### Ejemplo de Ejecución
```
=== SUPER CALCULADORA ===
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)
5. Potencia (**)
6. Raíz cuadrada (√)
7. Ver historial
8. Salir

Elige una opción: 4
Primer número: 10
Segundo número: 0
❌ Error: No se puede dividir por cero

Elige una opción: 6
Número: -4
❌ Error: No se puede calcular la raíz cuadrada de un número negativo

Elige una opción: 1
Primer número: 15
Segundo número: 27
✅ Resultado: 15 + 27 = 42

¿Deseas continuar? (s/n): s
```

## Soluciones

## Ejercicio 1: Conversor de Temperatura

```python
def validar_temperatura(celsius):
    """Valida que la temperatura no esté por debajo del cero absoluto."""
    if celsius < -273.15:
        print("❌ Error: La temperatura está por debajo del cero absoluto (-273.15°C)")
        return False
    return True

def convertir_celsius_a_fahrenheit(celsius):
    """Convierte la temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    print("=== CONVERSOR DE TEMPERATURA ===")

    try:
        # Solicitar la temperatura en Celsius
        celsius = float(input("Ingresa la temperatura en Celsius: "))

        # Validar la temperatura
        if not validar_temperatura(celsius):
            return  # Terminar si la temperatura no es válida

        # Realizar la conversión
        fahrenheit = convertir_celsius_a_fahrenheit(celsius)
        print(f"✅ {celsius}°C = {fahrenheit}°F")

    except ValueError:
        print("❌ Error: Debes ingresar un número válido")
    finally:
        print("🔚 Conversión finalizada")

# Llamar a la función principal
main()
```

## Ejercicio 2: Registro de Usuario

```python
def validar_nombre(nombre):
    """Valida que el nombre no esté vacío."""
    if nombre == "":
        print("❌ Error: El nombre no puede estar vacío")
        return False
    return True

def validar_edad(edad):
    """Valida que la edad esté dentro de un rango razonable."""
    if edad < 0 or edad > 120:
        print("❌ Error: La edad debe estar entre 0 y 120 años")
        return False
    return True

def validar_email(email):
    """Valida que el email tenga un formato básico."""
    if "@" not in email or "." not in email:
        print("❌ Error: Email inválido. Debe contener '@' y '.'")
        return False
    return True

def main():
    print("=== SISTEMA DE REGISTRO ===")

    try:
        # Pedir el nombre
        nombre = input("Nombre: ").strip()
        if not validar_nombre(nombre):
            return  # Terminar si el nombre no es válido

        # Pedir la edad
        edad = int(input("Edad: "))
        if not validar_edad(edad):
            return  # Terminar si la edad no es válida

        # Pedir el email
        email = input("Email: ").strip()
        if not validar_email(email):
            return  # Terminar si el email no es válido

        # Si todo está bien, mostrar los datos
        print("\n✅ Usuario registrado correctamente:")
        print(f"- Nombre: {nombre}")
        print(f"- Edad: {edad}")
        print(f"- Email: {email}")

    except ValueError:
        print("❌ Error: La edad debe ser un número")
    finally:
        print("\n🔚 Proceso de registro finalizado")

# Llamar a la función principal
main()
```

## Ejercicio 3: Calculadora Básica

```python
def mostrar_menu():
    """Muestra el menú de opciones de la calculadora."""
    print("=== CALCULADORA BÁSICA ===")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potencia (**)")
    print("6. Raíz cuadrada (√)")

def validar_opcion(opcion):
    """Valida que la opción esté dentro del rango permitido (1-6)."""
    if opcion < 1 or opcion > 6:
        print("❌ Error: Opción inválida")
        return False
    return True

def realizar_operacion(opcion, num1=None, num2=None):
    """Realiza la operación seleccionada y muestra el resultado."""
    if opcion == 1:
        resultado = num1 + num2
        print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")

    elif opcion == 2:
        resultado = num1 - num2
        print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")

    elif opcion == 3:
        resultado = num1 * num2
        print(f"\n✅ Resultado: {num1} * {num2} = {resultado}")

    elif opcion == 4:
        if num2 == 0:
            print("❌ Error: No se puede dividir por cero")
        else:
            resultado = num1 / num2
            print(f"\n✅ Resultado: {num1} / {num2} = {resultado:.2f}")

    elif opcion == 5:
        resultado = num1 ** num2
        print(f"\n✅ Resultado: {num1} ** {num2} = {resultado}")

    elif opcion == 6:
        if num1 < 0:
            print("❌ Error: No se puede calcular la raíz cuadrada de un número negativo")
        else:
            resultado = num1 ** 0.5
            print(f"\n✅ Resultado: √{num1} = {resultado:.2f}")

def main():
    mostrar_menu()

    try:
        # Pedir la opción al usuario
        opcion = int(input("\nElige una opción (1-6): "))

        # Validar la opción
        if not validar_opcion(opcion):
            return  # Terminar si la opción no es válida

        # Pedir números según la opción
        if opcion != 6:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
        else:
            num1 = float(input("Número: "))
            num2 = None  # No se necesita un segundo número para la raíz cuadrada

        # Realizar la operación
        realizar_operacion(opcion, num1, num2)

    except ValueError:
        print("❌ Error: Debes ingresar números válidos")
    finally:
        print("\n🔚 Operación finalizada")

# Llamar a la función principal
main()
```
