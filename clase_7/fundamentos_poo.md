# Programación Orientada a Objetos en Python

## 1. Explicación Teórica

### 1.1 Definición
En esta sección, comenzaremos a aprender un concepto llamado **Programación Orientada a Objetos (POO)**, conocido como **OOP** en inglés. La pregunta es: ¿por qué es importante aprenderlo?

La **programación procedural**, la que hemos venido utilizando hasta ahora, se basa en funciones que realizan tareas específicas y sigue un flujo lineal de ejecución (de arriba hacia abajo). Sin embargo, cuando los proyectos se vuelven más complejos, este estilo de programación puede dificultar el seguimiento y la organización del código.

La **programación procedural** es útil, pero tiene limitaciones, especialmente en proyectos grandes. Aquí es donde entra en juego la **Programación Orientada a Objetos (POO)**. Este paradigma nos permite dividir un proyecto complejo en partes más pequeñas y manejables, llamadas **objetos**, que pueden ser desarrollados por diferentes equipos de manera simultánea. Además, estos objetos son **reutilizables**, lo que significa que pueden ser utilizados en otros proyectos sin necesidad de reprogramarlos.

Para entender mejor la POO, imaginemos que estamos desarrollando un software para **robots inteligentes**. Este proyecto es complejo y requiere muchas funciones y procedimientos. En lugar de escribir todo el código de manera lineal, podemos dividir el robot en **modelos** o componentes, como el procesador, los sensores, el reconocimiento de voz, etc. Cada uno de estos modelos puede ser desarrollado por un equipo diferente, lo que aumenta la productividad y facilita la colaboración.

La POO también se puede comparar con la gestión de un **hotel**. Imagina que tienes que hacer todas las tareas del hotel tú solo: ser recepcionista, hacer la limpieza, cocinar y llevar la contabilidad. Sería casi imposible. En cambio, si contratas a personas especializadas en cada área, puedes delegar tareas y gestionar el hotel de manera más eficiente. De la misma manera, en POO, cada **objeto** tiene su propia funcionalidad y responsabilidad, lo que simplifica la gestión del código y lo hace más escalable.

En resumen, la POO nos permite:
1. **Dividir** proyectos complejos en partes más pequeñas y manejables
2. **Reutilizar** código en diferentes proyectos
3. **Organizar** el código de manera más eficiente, facilitando la colaboración y el mantenimiento


### 1.2 Fundamentos Clave
- **Clases**: Son los "planos" o "moldes" que definen las propiedades y comportamientos de un tipo de objeto
- **Objetos**: Son instancias específicas de una clase
- **Atributos**: Son las características o propiedades que tienen los objetos
- **Métodos**: Son las acciones que pueden realizar los objetos

### 1.3 Analogías y Ejemplos Conceptuales
Imagina una fábrica de coches:
- La **clase** sería el diseño del coche (plano)
- Cada **objeto** sería un coche específico fabricado
- Los **atributos** serían las características del coche (color, modelo, velocidad máxima)
- Los **métodos** serían las acciones que puede realizar (arrancar, acelerar, frenar)

## 2. Código de Demostración

### 2.1 Ejemplo Básico
```python
# Título: Creación de una clase Coche básica
# Objetivo: Demostrar la estructura básica de una clase y sus componentes

class Coche:
    # Constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, marca, modelo, color):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.velocidad = 0

    # Método para arrancar el coche
    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} {self.modelo} ha arrancado"
        return f"El coche ya estaba encendido"

    # Método para acelerar
    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            return f"Velocidad actual: {self.velocidad} km/h"
        return "Primero debes arrancar el coche"

# Crear una instancia (objeto) de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")
print(mi_coche.arrancar())
print(mi_coche.acelerar(20))
```

**Explicación Detallada de los Conceptos Fundamentales de la POO**

**La Palabra Reservada `self`**

En Python, `self` es como un nombre propio que permite a cada coche identificarse a sí mismo. Imagina que tienes dos coches idénticos en un estacionamiento. Cuando presionas el botón de arranque en un control remoto, necesitas asegurarte de que solo arranca tu coche, no todos los coches. `self` es ese identificador único que le dice a cada coche "tú eres tú".

Cuando escribimos `self.marca`, es como si el coche dijera "mi marca". Si tenemos dos objetos `coche1` y `coche2`, cada uno sabe cuál es su propia marca gracias a `self`. Es similar a cómo dos personas pueden tener el mismo nombre, pero cuando cada una dice "mi nombre", se refiere a sí misma.

**El Método `__init__` (Constructor)**

El método `__init__` es como la línea de ensamblaje de una fábrica de coches. Cuando una fábrica produce un coche nuevo, necesita configurar todas sus características iniciales: instalar el motor, pintar la carrocería, colocar los asientos, etc.

En nuestro código, cuando creamos un coche nuevo, `__init__` es el proceso que:
- Registra la marca, modelo y color del coche
- Asegura que el coche comience apagado (encendido = False)
- Establece la velocidad inicial en cero

El doble guion bajo en `__init__` es la forma que tiene Python de decir "este es un método especial que se ejecutará automáticamente al crear un coche nuevo".

**Atributos**

Los atributos son como las características físicas y el estado actual del coche. Son similares a las especificaciones que encontrarías en el manual del propietario:

- `marca`: es como el fabricante del coche (Toyota, Ford, etc.)
- `modelo`: es el tipo específico de coche (Corolla, Mustang, etc.)
- `color`: es el color de la carrocería
- `encendido`: es como la posición de la llave (encendido/apagado)
- `velocidad`: es como el número que marca el velocímetro

Cada uno de estos atributos puede cambiar durante la vida del coche. Por ejemplo, la velocidad cambiará mientras conduces.

**Métodos**

Los métodos son como los controles y funciones que tiene un coche. Así como un coche real tiene pedales, palancas y botones que realizan acciones, nuestra clase Coche tiene métodos que definen qué puede hacer:

- `arrancar()` es como girar la llave en el contacto
- `acelerar(incremento)` es como presionar el pedal del acelerador

Cada método puede:
- Verificar el estado actual del coche (¿está encendido?)
- Modificar sus atributos (cambiar la velocidad)
- Informar sobre lo que está sucediendo ("El coche ha arrancado")

**Instanciación**

Cuando escribimos `mi_coche = Coche("Toyota", "Corolla", "Rojo")`, es como ir a un concesionario y comprar un coche específico. No estamos comprando el diseño o los planos del coche, sino un coche real que podemos conducir.

Es similar a cómo una fábrica puede usar los mismos planos (la clase) para producir miles de coches (objetos), cada uno con sus propias características específicas pero siguiendo el mismo diseño básico.

**Uso del Objeto**

Una vez que tenemos nuestro coche (objeto), podemos interactuar con él de manera similar a como lo haríamos con un coche real:
- `mi_coche.arrancar()` es como girar la llave
- `mi_coche.acelerar(20)` es como presionar el acelerador
- `mi_coche.velocidad` es como mirar el velocímetro

Cada coche mantiene su propio estado independiente, igual que en la vida real: el hecho de que aceleres tu coche no hace que todos los demás coches del mismo modelo aceleren también.


### 2.2 Notas para el Instructor
- **Puntos clave a enfatizar:**
  1. El método `__init__` es el constructor y se llama automáticamente al crear un objeto
  2. `self` representa la instancia actual del objeto
  3. Los métodos pueden modificar los atributos del objeto
  4. La encapsulación permite mantener el estado interno del objeto

- **Posibles preguntas de los estudiantes:**
  1. "¿Por qué necesitamos usar 'self'?"
  2. "¿Cuándo se llama al método `__init__`?"
  3. "¿Podemos tener una clase sin atributos o sin métodos?"

- **Errores comunes a prevenir:**
  1. Olvidar incluir `self` como primer parámetro en los métodos
  2. Confundir métodos de clase con métodos de instancia
  3. No inicializar atributos en el constructor

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real: BankAccount
**Contexto**: Una cuenta de bnaco la podemos activar/desactivar y podemos hacer un depósito y sacar dinero
**Implementación**:
```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar, cuenta inactiva")

    def deactivate(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")

    def activate(self):
        self.is_active = True
        print("La cuenta ha sido activada")

# Crear objetos de la clase BankAccount
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)
cuenta1.activate()
cuenta1.deposit(200)

# Creación de cuentas
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

# Realización de operaciones
cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)  # No se puede depositar, cuenta inactiva
cuenta1.activate()
cuenta1.deposit(200)  # Depósito exitoso
```

**Puntos Importantes**:
- La clase mantiene el estado de la cuenta
- Los métodos validan el estado antes de realizar acciones
- Se implementa una lógica de negocio real

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico
**Ejercicio 1: Sistema de Biblioteca**
**Descripción**:
Crear una clase `Libro` que represente un libro en una biblioteca. Esta clase debe permitir:
- Registrar un nuevo libro con título, autor y año de publicación
- Prestar el libro a un usuario
- Devolver el libro a la biblioteca
- Consultar el estado actual del libro (disponible o prestado)

**Objetivo**:
Practicar los conceptos fundamentales de POO mediante la creación de una clase que modele un objeto de la vida real, implementando atributos y métodos básicos.

**Pistas**:
1. Piensa en qué atributos necesitas para rastrear:
   - La información básica del libro (título, autor, año)
   - Si el libro está prestado o no
   - Quién tiene el libro actualmente (si está prestado)

2. Para los métodos, considera:
   - ¿Puede prestarse un libro que ya está prestado?
   - ¿Puede devolverse un libro que no está prestado?
   - ¿Qué mensaje debe devolver cada operación?

### 4.2 Nivel Intermedio
**Ejercicio: Sistema de Inventario**
- **Descripción**: Crear una clase `Producto` y una clase `Inventario` que permita:
  - Agregar productos con cantidad
  - Realizar ventas
  - Verificar stock
  - Generar alertas de stock bajo
- **Objetivo**: Practicar la interacción entre múltiples clases
- **Pistas**:
  1. Usar una lista o diccionario en la clase Inventario para almacenar productos
  2. Implementar método para verificar stock antes de una venta
  3. Crear método para generar reporte de inventario


### 4.4 Soluciones y Explicaciones

En esta sección, veremos las soluciones detalladas de cada ejercicio, explicando paso a paso cómo se implementan los conceptos de la Programación Orientada a Objetos.

#### 4.4.1 Solución Nivel Básico: Sistema de Biblioteca

En este ejercicio, crearemos una clase para gestionar libros en una biblioteca. La solución implementa los conceptos básicos de POO de una manera clara y directa.

```python
class Libro:
    def __init__(self, titulo, autor, año):
        # Atributos básicos del libro
        self.titulo = titulo
        self.autor = autor
        self.año = año
        # Estado del libro
        self.prestado = False
        self.usuario_actual = None

    def prestar(self, nombre_usuario):
        # Verificamos si el libro está disponible
        if not self.prestado:
            self.prestado = True
            self.usuario_actual = nombre_usuario
            return f"Libro '{self.titulo}' prestado a {nombre_usuario}"
        else:
            return f"El libro '{self.titulo}' ya está prestado a {self.usuario_actual}"

    def devolver(self):
        # Verificamos si el libro estaba prestado
        if self.prestado:
            self.prestado = False
            usuario_anterior = self.usuario_actual
            self.usuario_actual = None
            return f"Libro '{self.titulo}' devuelto por {usuario_anterior}"
        else:
            return f"El libro '{self.titulo}' no estaba prestado"

    def obtener_estado(self):
        estado = "prestado" if self.prestado else "disponible"
        info = f"Libro: {self.titulo}\nAutor: {self.autor}\nAño: {self.año}\nEstado: {estado}"
        if self.prestado:
            info += f"\nPrestado a: {self.usuario_actual}"
        return info

# Ejemplo de uso:
libro = Libro("Don Quijote", "Miguel de Cervantes", 1605)
print(libro.prestar("Ana García"))  # Préstamo exitoso
print(libro.prestar("Juan López"))  # Intento fallido
print(libro.obtener_estado())       # Ver estado actual
print(libro.devolver())             # Devolución exitosa
```

La solución demuestra varios conceptos fundamentales:

1. **Encapsulamiento**: Los datos (atributos) y las operaciones (métodos) están juntos en la clase.
2. **Estado del objeto**: El libro mantiene información sobre si está prestado y a quién.
3. **Validaciones**: Cada método verifica condiciones antes de realizar operaciones.

#### 4.4.2 Solución Nivel Intermedio: Sistema de Inventario

Este ejercicio introduce la interacción entre múltiples clases y el manejo de colecciones de objetos.

```python
class Producto:
    def __init__(self, codigo, nombre, precio, stock_minimo=5):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock_actual = 0
        self.stock_minimo = stock_minimo

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}) - Stock: {self.stock_actual}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def agregar_producto(self, producto, cantidad):
        if producto.codigo in self.productos:
            self.productos[producto.codigo].stock_actual += cantidad
            return f"Stock actualizado para {producto.nombre}"
        else:
            producto.stock_actual = cantidad
            self.productos[producto.codigo] = producto
            return f"Nuevo producto agregado: {producto.nombre}"

    def realizar_venta(self, codigo, cantidad):
        if codigo not in self.productos:
            return "Producto no encontrado"

        producto = self.productos[codigo]
        if producto.stock_actual >= cantidad:
            producto.stock_actual -= cantidad
            if self.verificar_stock_bajo(codigo):
                return f"Venta realizada. ALERTA: Stock bajo en {producto.nombre}"
            return "Venta realizada exitosamente"
        return "Stock insuficiente"

    def verificar_stock_bajo(self, codigo):
        producto = self.productos[codigo]
        return producto.stock_actual < producto.stock_minimo

    def generar_reporte(self):
        reporte = "=== Reporte de Inventario ===\n"
        for producto in self.productos.values():
            estado = "STOCK BAJO" if self.verificar_stock_bajo(producto.codigo) else "OK"
            reporte += f"{producto.nombre}:\n"
            reporte += f"  Stock actual: {producto.stock_actual}\n"
            reporte += f"  Estado: {estado}\n"
        return reporte

# Ejemplo de uso:
inventario = Inventario()
laptop = Producto("LAP001", "Laptop Gaming", 1200.0)
mouse = Producto("MOU001", "Mouse Inalámbrico", 25.0)

print(inventario.agregar_producto(laptop, 10))
print(inventario.agregar_producto(mouse, 20))
print(inventario.realizar_venta("LAP001", 8))
print(inventario.generar_reporte())
```

Esta solución demuestra:

1. **Relaciones entre clases**: Producto e Inventario trabajan juntos.
2. **Gestión de colecciones**: Uso de diccionarios para almacenar objetos.
3. **Lógica de negocio**: Manejo de stock y alertas.


Cada solución representa un nivel diferente de complejidad en POO:
- El nivel básico introduce los conceptos fundamentales de manera accesible
- El nivel intermedio añade interacciones entre clases y manejo de datos

## 5. Recursos Adicionales
- **Documentación oficial**: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- **Artículos relacionados**: Real Python - [OOP in Python](https://realpython.com/python3-object-oriented-programming/)


