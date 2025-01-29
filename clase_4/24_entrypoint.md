# ¿Qué es `if __name__ == "__main__":`?

En Python, el código `if __name__ == "__main__":` es una construcción muy útil que nos permite controlar cómo se ejecuta nuestro script. Aunque puede parecer un poco confuso al principio, es una herramienta importante para escribir programas más organizados y reutilizables.

## ¿Para qué sirve?

Cuando escribimos un programa en Python, a veces queremos que ciertas partes del código **solo se ejecuten si el archivo se está ejecutando directamente**, y no cuando se importa como un módulo en otro script. Esto es especialmente útil cuando creamos funciones o clases que queremos reutilizar en otros programas.

### Ejemplo básico

Imagina que tienes un archivo llamado `mi_script.py` con el siguiente código:

```python
def saludar():
    print("¡Hola desde mi_script!")

print("Este mensaje se muestra siempre.")
```

Si ejecutas este archivo directamente, verás:

```
Este mensaje se muestra siempre.
```

Pero si importas `mi_script` en otro archivo, como `otro_script.py`:

```python
import mi_script

mi_script.saludar()
```

Al ejecutar `otro_script.py`, verás:

```
Este mensaje se muestra siempre.
¡Hola desde mi_script!
```

¿Notas el problema? El mensaje `"Este mensaje se muestra siempre."` se imprime incluso cuando solo queríamos usar la función `saludar()`. Aquí es donde entra en juego `if __name__ == "__main__":`.

---

## ¿Cómo funciona `if __name__ == "__main__":`?

En Python, cada archivo tiene una variable especial llamada `__name__`. Cuando ejecutas un archivo directamente, Python asigna a `__name__` el valor `"__main__"`. Sin embargo, si el archivo se importa como un módulo, `__name__` toma el nombre del archivo (sin la extensión `.py`).

Podemos usar esto para controlar qué código se ejecuta en cada caso.

### Ejemplo mejorado

Modifiquemos `mi_script.py`:

```python
def saludar():
    print("¡Hola desde mi_script!")

if __name__ == "__main__":
    print("Este mensaje solo se muestra si ejecutas mi_script directamente.")
```

Ahora, si ejecutas `mi_script.py` directamente, verás:

```
Este mensaje solo se muestra si ejecutas mi_script directamente.
```

Pero si importas `mi_script` en `otro_script.py`:

```python
import mi_script

mi_script.saludar()
```

Al ejecutar `otro_script.py`, verás solo:

```
¡Hola desde mi_script!
```

¡El mensaje adicional ya no se muestra! Esto ocurre porque el código dentro del bloque `if __name__ == "__main__":` solo se ejecuta cuando el archivo se ejecuta directamente.

---

## ¿Por qué es útil?

1. **Reutilización de código**: Si escribes funciones o clases en un archivo, puedes importarlas en otros scripts sin que se ejecute código innecesario.
2. **Organización**: Separa claramente la lógica principal del script de las funciones o clases que defines.
3. **Pruebas**: Puedes incluir pruebas o ejemplos dentro del bloque `if __name__ == "__main__":` para probar tu código sin afectar su uso en otros programas.

---

## Resumen

- `if __name__ == "__main__":` es una forma de controlar qué código se ejecuta cuando un archivo se ejecuta directamente.
- `__name__` es una variable especial que Python asigna automáticamente.
  - Si el archivo se ejecuta directamente, `__name__` es `"__main__"`.
  - Si el archivo se importa como módulo, `__name__` es el nombre del archivo.
- Usar `if __name__ == "__main__":` hace que tu código sea más modular, reutilizable y organizado.

### Ejemplo final

```python
def main():
    print("Este es el programa principal.")

if __name__ == "__main__":
    main()
```

En este caso, la función `main()` solo se ejecutará si el archivo se ejecuta directamente. Si se importa, no pasará nada.
