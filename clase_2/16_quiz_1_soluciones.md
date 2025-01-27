# Quiz 1: Soluciones
## Parte 1: Selección Múltiple
1. b) HolaPython
   - Explicación: El operador + concatena strings sin agregar espacios

2. b) 15.5
   - Explicación: float("5.5") convierte "5.5" a número decimal y luego suma 10

3. c) str
   - Explicación: input() siempre devuelve un string

4. b) 3
   - Explicación: // es división entera, devuelve solo la parte entera del resultado

5. b) 14
   - Explicación: Por jerarquía, primero se hace 3 * 4 = 12, luego 2 + 12 = 14

## Parte 2: Verdadero o Falso
6. FALSO
   - Explicación: Compara tipos diferentes (int vs str)

7. VERDADERO
   - Explicación: El operador + concatena strings

8. VERDADERO
   - Explicación: 10 dividido entre 3 da 3 con resto 1

9. FALSO
   - Explicación: input() devuelve str, hay que convertir para operaciones matemáticas

10. FALSO
   - Explicación: Repite el string 3 veces: "HolaHolaHola"

## Parte 3: Análisis de Código
11. Solución:
```python
edad = int(input("Tu edad: "))
siguiente_edad = edad + 1
print(siguiente_edad)
```
- Error: No se convierte el input a int antes de sumar

12. Solución:
```python
minutos = 58
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{horas} horas y {minutos_restantes} minutos")
```

13. Resultados:
```python
False  # 10 > 5 es True, pero 4 < 3 es False, True and False = False
True   # 10 > 5 es True, por lo que ya no importa 4 < 3
False  # 10 > 5 es True, not True = False
```

## Parte 4: Ejercicios Prácticos
14. Solución:
```python
numero = int(input("Ingresa un número: "))
es_par = numero % 2 == 0
es_positivo = numero > 0
resultado = es_par and es_positivo
print(f"¿El número es par y positivo? {resultado}")
```

15. Solución:
```python
numero = int(input("Ingresa un número: "))
esta_en_rango = 1 <= numero <= 100
print(f"¿El número está entre 1 y 100? {esta_en_rango}")
```
