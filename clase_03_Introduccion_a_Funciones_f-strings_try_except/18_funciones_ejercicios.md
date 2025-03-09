# 🐍 Ejercicios de Funciones en Python

## 📝 Ejercicio 1: Calculadora de Descuentos

### Enunciado
Crear un programa que calcule el precio final de un producto con descuento. Debes crear funciones para:
1. Validar que el descuento esté entre 0 y 100
2. Calcular el precio con el descuento aplicado
3. Mostrar el ahorro total

### Ejemplo de Ejecución
```
=== CALCULADORA DE DESCUENTOS ===
Ingrese el precio del producto: 100
Ingrese el porcentaje de descuento: 20

-- Resumen de la compra --
Precio original: $100.00
Descuento: 20%
Ahorro: $20.00
Precio final: $80.00

=== CALCULADORA DE DESCUENTOS ===
Ingrese el precio del producto: 50
Ingrese el porcentaje de descuento: 150
Error: El descuento debe estar entre 0 y 100
```

### Solución: Calculadora de Descuentos
```python
def validar_descuento(descuento):
    """Valida que el descuento esté entre 0 y 100"""
    return 0 <= descuento <= 100

def calcular_precio_con_descuento(precio, descuento):
    """Calcula el precio final después del descuento"""
    return precio - (precio * descuento / 100)

def calcular_ahorro(precio, precio_final):
    """Calcula el monto total ahorrado"""
    return precio - precio_final

def mostrar_resumen(precio, descuento):
    """Muestra el resumen de la compra"""
    if not validar_descuento(descuento):
        print("Error: El descuento debe estar entre 0 y 100")
        return

    precio_final = calcular_precio_con_descuento(precio, descuento)
    ahorro = calcular_ahorro(precio, precio_final)

    print("\n-- Resumen de la compra --")
    print(f"Precio original: ${precio:.2f}")
    print(f"Descuento: {descuento}%")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Precio final: ${precio_final:.2f}")

# Programa principal
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
mostrar_resumen(precio, descuento)
```

## 📝 Ejercicio 2: Validador de Contraseñas

### Enunciado
Desarrollar un programa que verifique si una contraseña cumple con los siguientes criterios:
1. Longitud mínima de 8 caracteres
2. Al menos una letra mayúscula
3. Al menos un número

### Ejemplo de Ejecución
```
=== VALIDADOR DE CONTRASEÑAS ===
Ingrese su contraseña: abc123
❌ La contraseña no cumple los requisitos:
- Debe tener al menos 8 caracteres
- Debe contener al menos una mayúscula

=== VALIDADOR DE CONTRASEÑAS ===
Ingrese su contraseña: Abc12345
✅ Contraseña válida! Cumple todos los requisitos:
- Longitud adecuada
- Contiene mayúsculas
- Contiene números
```
