# 🤖 Guía: Reeborg's World - Introducción a la Programación

## 📝 ¿Qué es Reeborg's World?
Reeborg's World es una plataforma web interactiva que ayuda a aprender programación a través de un robot que podemos controlar con código Python. El robot puede moverse, girar y realizar diferentes acciones en un mundo virtual.

## 🔍 Comandos Básicos
```python
# Movimientos básicos del robot
move()       # Mover adelante
turn_left()  # Girar a la izquierda
```

## 🛠️ Funciones Personalizadas
### Ejemplo: Girar a la Derecha
```python
def turn_right():
    turn_left()    # Como no existe turn_right()
    turn_left()    # lo creamos usando tres
    turn_left()    # giros a la izquierda
```

### Ejemplo: Función de Salto
```python
def jump():
    move()         # Avanzar
    turn_left()    # Girar izquierda
    move()         # Subir
    turn_right()   # Girar derecha
    move()         # Avanzar sobre obstáculo
    turn_right()   # Girar derecha
    move()         # Bajar
    turn_left()    # Orientarse de nuevo
```

## 💡 Conceptos Clave
1. **Definición de Funciones**
   - Usar `def` para crear nuevas funciones
   - Dar nombres descriptivos
   - Identar correctamente el código

2. **Reutilización de Código**
   - Crear una función una vez
   - Usarla múltiples veces
   - Evitar repetir código

3. **Secuencia de Instrucciones**
   - Las instrucciones se ejecutan en orden
   - Una línea tras otra
   - De arriba hacia abajo

## 🎯 Ejemplo de Solución
```python
def turn_right():
   turn_left()
   turn_left()
   turn_left()

def jump():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()

jump()
jump()
jump()
jump()
jump()
jump()
```

## 🎮 Enlaces Útiles
- [Reeborg's World](http://reeborg.ca/reeborg.html)
- [Documentación de Reeborg](http://reeborg.ca/docs/en/)
