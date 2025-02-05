# Herencia en Python

## 1. Explicación Teórica

### 1.1 Introducción y Definición

La herencia es uno de los conceptos fundamentales de la Programación Orientada a Objetos (POO). Imaginemos que estamos organizando una tienda de vehículos. En lugar de escribir código separado para coches, motos y camiones, que comparten muchas características comunes, podemos crear una "plantilla base" (clase padre) llamada `Vehicle` que contenga todas las características y comportamientos comunes, y luego crear clases específicas (clases hijas) que hereden estas características y añadan sus propias particularidades.

La herencia permite:
- Reutilizar código de manera eficiente
- Establecer una jerarquía clara entre clases
- Implementar comportamientos generales que pueden ser especializados

### 1.2 Fundamentos Clave

La herencia en Python se basa en varios conceptos importantes:

1. **Clase Base (Padre)**: Define las características y comportamientos comunes.
2. **Clase Derivada (Hija)**: Hereda de la clase base y puede añadir o modificar funcionalidades.
3. **Método `super()`**: Permite acceder a los métodos de la clase padre.
4. **Sobrescritura de métodos**: Permite modificar el comportamiento heredado.

### 1.3 Analogías y Ejemplos Conceptuales

Imaginemos una concesionaria de vehículos:

1. **Clase Base (Vehicle)**:
   - Como un "blueprint" general de vehículos
   - Define características comunes: marca, modelo, precio
   - Define comportamientos comunes: vender, verificar disponibilidad

2. **Clases Derivadas (Car, Bike, Truck)**:
   - Como "especializaciones" del blueprint general
   - Heredan características básicas
   - Añaden características específicas
   - Pueden modificar comportamientos según necesidades

## 2. Código de Demostración

### 2.1 Ejemplo Básico
```python
class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No está disponible")

    # Abstracción
    def check_available(self):
        return self.is_available

    #Abstracción
    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

# Herencia
class Car(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} estÃ¡ en marcha"
        else:
            return f"El coche {self.brand} no estÃ¡ disponible"

    # Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No estÃ¡ disponible"

# Herencia
class Bike(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

     # Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No está disponible"

# Herencia
class Truck(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camiÃ³n {self.brand} está en marcha"
        else:
            return f"El camiÃ³n {self.brand} no está disponible"

    # Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No está disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento,{vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()
```

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real: Concesionario
```python
# Ejemplo de uso del sistema
car = Car("Toyota", "Corolla", 20000)
bike = Bike("Yamaha", "MT-07", 7000)

# La misma interfaz funciona para diferentes tipos de vehículos
car.sell()
bike.sell()

print(car.start_engine())  # Método específico de Car
print(bike.start_engine()) # Método específico de Bike
```

**Puntos Importantes**:
- La herencia permite tratar diferentes tipos de vehículos de manera uniforme
- Cada clase puede tener su propia implementación específica
- El código es más mantenible y organizado

## 4. Ejercicios Propuestos

### 4.1 Nivel Básico: Sistema de Empleados Corporativos

En este ejercicio, desarrollaremos un sistema para gestionar diferentes tipos de empleados en una empresa. Este sistema nos ayudará a entender los conceptos básicos de la herencia y el polimorfismo.

**Objetivo Principal**:
Crear un sistema que permita gestionar diferentes tipos de empleados y calcular sus salarios según sus características específicas.

**Requisitos Detallados**:

1. **Clase Base Employee**:
   - Atributos obligatorios:
     - ID del empleado
     - Nombre completo
     - Fecha de contratación
     - Salario base
   - Métodos necesarios:
     - Constructor con validaciones
     - Cálculo de años de antigüedad
     - Método abstracto para cálculo de salario

2. **Tipos de Empleados a Implementar**:
   - Empleado a Tiempo Completo:
     - Salario base + bonus por antigüedad (5% por año)
   - Empleado a Tiempo Parcial:
     - Salario calculado por horas trabajadas
   - Empleado por Comisiones:
     - Salario base + porcentaje de ventas

3. **Funcionalidades Adicionales**:
   - Mostrar información detallada del empleado
   - Validar que los salarios no sean negativos
   - Implementar formato adecuado para mostrar salarios

### 4.2 Nivel Intermedio: Sistema de Formas Geométricas

En este ejercicio, crearemos un sistema para trabajar con diferentes formas geométricas, aplicando conceptos más avanzados de herencia y validaciones.

**Objetivo Principal**:
Desarrollar un sistema que permita calcular áreas y perímetros de diferentes formas geométricas, asegurando la validez de las formas creadas.

**Requisitos Detallados**:

1. **Clase Base Shape**:
   - Métodos abstractos:
     - Cálculo de área
     - Cálculo de perímetro
     - Descripción de la forma
   - Validaciones genéricas

2. **Formas a Implementar**:
   - Círculo:
     - Validar radio positivo
     - Usar math.pi para cálculos precisos
   - Rectángulo:
     - Validar base y altura positivas
     - Incluir caso especial para cuadrados
   - Triángulo:
     - Validar que los tres lados puedan formar un triángulo
     - Implementar fórmula de Herón para el área

3. **Funcionalidades Adicionales**:
   - Sistema para comparar formas por área
   - Método para verificar si una forma es regular
   - Generación de reportes formatados

### 4.3 Nivel Avanzado: Sistema de Juego RPG

En este ejercicio, desarrollaremos un sistema de juego completo que demuestre el uso avanzado de la programación orientada a objetos.

**Objetivo Principal**:
Crear un sistema de juego con diferentes tipos de personajes que puedan interactuar entre sí, usando conceptos avanzados de POO.

**Requisitos Detallados**:

1. **Clase Base Character**:
   - Atributos base:
     - Nombre
     - Puntos de vida
     - Nivel
     - Estado (vivo/derrotado)
     - Lista de habilidades
   - Métodos abstractos:
     - Ataque básico
     - Habilidad especial
   - Métodos comunes:
     - Recibir daño
     - Curación
     - Mostrar estado

2. **Tipos de Personajes**:
   - Guerrero:
     - Mayor vida y daño físico
     - Sistema de furia para habilidades especiales
   - Mago:
     - Daño mágico elevado pero poca vida
     - Sistema de maná para hechizos
   - Pícaro:
     - Daño moderado pero ataques rápidos
     - Sistema de energía para habilidades

3. **Sistema de Interacción**:
   - Implementar sistema de turnos
   - Calcular daño con elementos aleatorios
   - Gestionar estados especiales (aturdido, envenenado, etc.)
   - Sistema de experiencia y nivel

4. **Funcionalidades Adicionales**:
   - Sistema de inventario básico
   - Guardado y carga de estado de personajes
   - Registro de combates
   - Sistema de logros

**Nota**: Para todos los ejercicios, se valorará:
- Documentación clara del código
- Manejo adecuado de errores
- Código limpio y bien organizado


## 5. Recursos Adicionales
- **Documentación oficial**: [Python Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- **Artículos recomendados**: Real Python - [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- **Ejercicios adicionales**: [Python OOP Exercises](https://www.w3resource.com/python-exercises/class-exercises/)


## 6. Soluciones de Ejercicios

### 6.1 Sistema de Empleados (Nivel Básico)

```python
from abc import ABC, abstractmethod
from datetime import datetime

class Employee(ABC):
    """
    Clase base abstracta para todos los empleados.
    Define la estructura común y comportamientos que todos los empleados deben tener.
    """
    def __init__(self, id: str, name: str, base_salary: float):
        self.id = id
        self.name = name
        self.base_salary = base_salary
        self.hire_date = datetime.now()

    @abstractmethod
    def calculate_salary(self) -> float:
        """
        Método abstracto que cada tipo de empleado debe implementar
        para calcular su salario específico.
        """
        pass

    def get_years_of_service(self) -> int:
        """
        Calcula los años de servicio del empleado.
        """
        years = datetime.now().year - self.hire_date.year
        return years

class FullTimeEmployee(Employee):
    """
    Empleado a tiempo completo con salario base y bonus por antigüedad.
    """
    def __init__(self, id: str, name: str, base_salary: float,
                 bonus_percentage: float = 0.05):
        super().__init__(id, name, base_salary)
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self) -> float:
        """
        Calcula el salario incluyendo bonus por años de servicio.
        """
        years = self.get_years_of_service()
        bonus = self.base_salary * self.bonus_percentage * years
        return self.base_salary + bonus

class PartTimeEmployee(Employee):
    """
    Empleado a tiempo parcial con salario basado en horas trabajadas.
    """
    def __init__(self, id: str, name: str, base_salary: float,
                 hours_worked: float):
        super().__init__(id, name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        """
        Calcula el salario basado en las horas trabajadas.
        """
        return self.base_salary * self.hours_worked

class CommissionEmployee(Employee):
    """
    Empleado con salario base más comisiones por ventas.
    """
    def __init__(self, id: str, name: str, base_salary: float,
                 sales: float, commission_rate: float = 0.02):
        super().__init__(id, name, base_salary)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self) -> float:
        """
        Calcula el salario incluyendo comisiones por ventas.
        """
        commission = self.sales * self.commission_rate
        return self.base_salary + commission

# Ejemplo de uso del sistema
def demonstrate_employee_system():
    # Crear diferentes tipos de empleados
    full_time = FullTimeEmployee("FT001", "Ana García", 3000)
    part_time = PartTimeEmployee("PT001", "Juan López", 15, 80)
    sales = CommissionEmployee("S001", "María Rodríguez", 2000, 50000)

    # Mostrar información y salarios
    employees = [full_time, part_time, sales]
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"\nEmpleado: {emp.name} ({emp.__class__.__name__})")
        print(f"ID: {emp.id}")
        print(f"Salario calculado: ${salary:.2f}")

if __name__ == "__main__":
    demonstrate_employee_system()
```

### 6.2 Sistema de Formas Geométricas (Nivel Intermedio)

```python
from abc import ABC, abstractmethod
import math
from typing import Optional

class Shape(ABC):
    """
    Clase base abstracta para todas las formas geométricas.
    Define la interfaz común que todas las formas deben implementar.
    """
    @abstractmethod
    def area(self) -> float:
        """Calcula el área de la forma."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calcula el perímetro de la forma."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Proporciona una descripción de la forma."""
        pass

class Circle(Shape):
    """
    Implementación de un círculo.
    """
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("El radio debe ser positivo")
        self.radius = radius

    def area(self) -> float:
        """Calcula el área del círculo: πr²"""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Calcula el perímetro del círculo: 2πr"""
        return 2 * math.pi * self.radius

    def describe(self) -> str:
        return f"Círculo de radio {self.radius}"

class Rectangle(Shape):
    """
    Implementación de un rectángulo.
    """
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Las dimensiones deben ser positivas")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calcula el área del rectángulo: base × altura"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calcula el perímetro del rectángulo: 2(base + altura)"""
        return 2 * (self.width + self.height)

    def describe(self) -> str:
        return f"Rectángulo de {self.width}×{self.height}"

class Triangle(Shape):
    """
    Implementación de un triángulo.
    """
    def __init__(self, a: float, b: float, c: float):
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Las medidas no forman un triángulo válido")
        self.a = a
        self.b = b
        self.c = c

    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        """
        Verifica si tres lados pueden formar un triángulo válido
        usando la desigualdad triangular.
        """
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and b + c > a and a + c > b)

    def area(self) -> float:
        """
        Calcula el área usando la fórmula de Herón.
        """
        s = (self.a + self.b + self.c) / 2  # Semiperímetro
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Calcula el perímetro sumando todos los lados."""
        return self.a + self.b + self.c

    def describe(self) -> str:
        return f"Triángulo de lados {self.a}, {self.b}, {self.c}"

def demonstrate_shapes():
    # Crear diferentes formas
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

    # Mostrar información de cada forma
    for shape in shapes:
        print(f"\n{shape.describe()}")
        print(f"Área: {shape.area():.2f}")
        print(f"Perímetro: {shape.perimeter():.2f}")

if __name__ == "__main__":
    demonstrate_shapes()
```

### 6.3 Sistema de Juego (Nivel Avanzado)

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import random

class Character(ABC):
    """
    Clase base abstracta para todos los personajes del juego.
    """
    def __init__(self, name: str, health: int, level: int = 1):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.level = level
        self.is_alive = True
        self.abilities: List[str] = []

    @abstractmethod
    def basic_attack(self, target: 'Character') -> str:
        """Ataque básico que todos los personajes deben implementar."""
        pass

    @abstractmethod
    def special_ability(self, target: Optional['Character'] = None) -> str:
        """Habilidad especial única para cada tipo de personaje."""
        pass

    def take_damage(self, amount: int) -> None:
        """
        Procesa el daño recibido y actualiza el estado del personaje.
        """
        self.current_health = max(0, self.current_health - amount)
        if self.current_health == 0:
            self.is_alive = False

    def heal(self, amount: int) -> None:
        """
        Restaura salud sin exceder el máximo.
        """
        if self.is_alive:
            self.current_health = min(self.max_health,
                                    self.current_health + amount)

    def get_status(self) -> str:
        """
        Retorna el estado actual del personaje.
        """
        status = "vivo" if self.is_alive else "derrotado"
        return (f"{self.name} (Nivel {self.level}): {self.current_health}/"
                f"{self.max_health} HP - {status}")

class Warrior(Character):
    """
    Guerrero: Especialista en combate cuerpo a cuerpo.
    """
    def __init__(self, name: str):
        super().__init__(name, health=120, level=1)
        self.abilities = ["Golpe Poderoso", "Grito de Guerra"]
        self.rage = 0

    def basic_attack(self, target: Character) -> str:
        damage = 15 + self.level * 2
        target.take_damage(damage)
        self.rage += 10
        return f"{self.name} ataca a {target.name} causando {damage} de daño"

    def special_ability(self, target: Character) -> str:
        if self.rage >= 30:
            damage = 25 + self.level * 3
            target.take_damage(damage)
            self.rage = 0
            return f"{self.name} usa Golpe Poderoso en {target.name} causando {damage} de daño"
        return f"{self.name} no tiene suficiente furia para usar Golpe Poderoso"

class Mage(Character):
    """
    Mago: Especialista en ataques mágicos y apoyo.
    """
    def __init__(self, name: str):
        super().__init__(name, health=80, level=1)
        self.abilities = ["Bola de Fuego", "Curación"]
        self.mana = 100

    def basic_attack(self, target: Character) -> str:
        damage = 10 + self.level * 1.5
        target.take_damage(int(damage))
        self.mana += 10
        return f"{self.name} lanza un proyectil mágico a {target.name} causando {int(damage)} de daño"

    def special_ability(self, target: Optional[Character] = None) -> str:
        if self.mana >= 40:
            if target:
                # Bola de Fuego
                damage = 30 + self.level * 4
                target.take_damage(int(damage))
                self.mana -= 40
                return f"{self.name} lanza Bola de Fuego a {target.name} causando {int(damage)} de daño"
            else:
                # Curación
                healing = 20 + self.level * 2
                self.heal(int(healing))
                self.mana -= 40
                return f"{self.name} se cura por {healing} puntos de vida"
        return f"{self.name} no tiene suficiente maná"

class Rogue(Character):
    """
    Pícaro: Especialista en ataques rápidos y evasión.
    """
    def __init__(self, name: str):
        super().__init__(name, health=90, level=1)
        self.abilities = ["Ataque Furtivo", "Evasión"]
        self.energy = 100

    def basic_attack(self, target: Character) -> str:
        damage = 12 + self.level * 1.8
        target.take_damage(int(damage))
        self.energy += 15
        return f"{self.name} apuñala a {target.name} causando {int(damage)} de daño"

    def special_ability(self, target: Character) -> str:
        if self.energy >= 50:
            damage = 35 + self.level * 3
            if random.random() < 0.2:  # 20% de golpe crítico
                damage *= 2
                target.take_damage(int(damage))
                self.energy -= 50
                return f"{self.name} realiza un Ataque Furtivo CRÍTICO a {target.name} causando {int(damage)} de daño"
            target.take_damage(int(damage))
            self.energy -= 50
            return f"{self.name} realiza un Ataque Furtivo a {target.name} causando {int(damage)} de daño"
        return f"{self.name} no tiene suficiente energía"

def demonstrate_game_system():
    # Crear personajes
    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    rogue = Rogue("Ezio")

    # Simular algunas interacciones
    print("=== Inicio de la batalla ===")
    print(warrior.get_status())
    print(mage.get_status())
    print(rogue.get_status())

    print("\n=== Ronda 1 ===")
    print(warrior.basic_attack(mage))
    print(mage.special_ability(warrior))
    print(rogue.basic_attack(warrior))

    print("\n=== Estado después de la Ronda 1 ===")
    print(warrior.get_status())
    print(mage.get_status())
    print(rogue.get_status())

    print("\n=== Ronda 2 ===")
    print(warrior.special_ability(rogue))
    print(mage.special_ability())  # Curación
    print(rogue.special_ability(warrior))

    print("\n=== Estado Final ===")
    print(warrior.get_status())
    print(mage.get_status())
    print(rogue.get_status())

if __name__ == "__main__":
    demonstrate_game_system()
```
