# Abstracción en Python

## 1. Explicación Teórica

### 1.1 Introducción y Definición

La abstracción es uno de los pilares fundamentales de la Programación Orientada a Objetos. Es el proceso de identificar las características y comportamientos esenciales de un objeto, ignorando los detalles innecesarios. Imagina un control remoto de televisión: no necesitas saber exactamente cómo funciona internamente para usarlo; solo necesitas conocer qué hacen sus botones.

En programación, la abstracción nos permite:
- Simplificar problemas complejos
- Ocultar detalles de implementación
- Enfocarnos en qué hace algo, no en cómo lo hace
- Crear interfaces claras y fáciles de usar

### 1.2 Fundamentos Clave

En Python, la abstracción se implementa principalmente a través de:

1. **Clases Abstractas**: Plantillas que definen qué métodos debe tener una clase
2. **Métodos Abstractos**: Métodos que deben ser implementados por las clases hijas
3. **Interfaces**: Contratos que especifican qué métodos debe tener una clase
4. **Encapsulamiento**: Ocultamiento de los detalles internos de implementación

### 1.3 Analogías y Ejemplos Conceptuales

Imaginemos una cafetería moderna con una máquina de café:

1. **Interfaz de Usuario** (Abstracción):
   - Botones para diferentes tipos de café
   - Pantalla con opciones
   - Indicadores de estado

2. **Mecanismo Interno** (Implementación):
   - Sistema de calentamiento de agua
   - Molinillo de café
   - Sistema de presión
   - Circuitos electrónicos

El cliente solo necesita conocer la interfaz (botones y pantalla) para obtener su café, sin necesidad de entender la complejidad interna de la máquina.

## 2. Código de Demostración

### 2.1 Ejemplo Básico
```python
from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    """
    Clase abstracta que define la interfaz de una máquina de café
    """
    def __init__(self):
        self.water_level = 100
        self.coffee_beans = 100

    @abstractmethod
    def make_coffee(self, coffee_type):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass

    @abstractmethod
    def clean(self):
        """Método abstracto para la limpieza de la máquina"""
        pass

    # Método concreto que todas las máquinas comparten
    def check_resources(self):
        return {
            'water': self.water_level,
            'coffee': self.coffee_beans
        }

class BasicCoffeeMachine(CoffeeMachine):
    """
    Implementación concreta de una máquina de café básica
    """
    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            self.water_level -= 30
            self.coffee_beans -= 20
            return "☕ Espresso preparado"
        elif coffee_type == "americano":
            self.water_level -= 50
            self.coffee_beans -= 15
            return "☕ Americano preparado"
        else:
            return "Tipo de café no disponible"

    def clean(self):
        return "Limpieza básica completada"

class PremiumCoffeeMachine(CoffeeMachine):
    """
    Implementación concreta de una máquina de café premium
    """
    def __init__(self):
        super().__init__()
        self.milk_level = 100

    def make_coffee(self, coffee_type):
        if coffee_type == "latte":
            self.water_level -= 30
            self.coffee_beans -= 20
            self.milk_level -= 50
            return "☕ Latte preparado"
        elif coffee_type == "cappuccino":
            self.water_level -= 30
            self.coffee_beans -= 20
            self.milk_level -= 30
            return "☕ Cappuccino preparado"
        else:
            return super().make_coffee(coffee_type)

    def clean(self):
        return "Limpieza premium con desinfección de sistema de leche completada"
```

## 3. Ejemplos Prácticos

### 3.1 Caso de Uso Real: Sistema de Notificaciones
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def verify_status(self):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        return f"Enviando email: {message}"

    def verify_status(self):
        return "Conexión al servidor de email OK"

class SMSNotifier(Notifier):
    def send(self, message):
        return f"Enviando SMS: {message}"

    def verify_status(self):
        return "Conexión al servicio SMS OK"

# Sistema que usa las notificaciones
def send_notification(notifier: Notifier, message: str):
    if notifier.verify_status():
        return notifier.send(message)
    return "Error: No se pudo enviar la notificación"

# Uso
email = EmailNotifier()
sms = SMSNotifier()

print(send_notification(email, "¡Hola por email!"))
print(send_notification(sms, "¡Hola por SMS!"))
```

**Puntos Importantes**:
- La abstracción permite cambiar implementaciones sin modificar el código cliente
- Cada clase concreta puede tener su propia implementación específica
- El sistema principal no necesita conocer los detalles de cada tipo de notificación

## 4. Ejercicios Propuestos

## 4. Ejercicios Propuestos - Sistemas Multimedia y Pagos

En esta sección, trabajaremos con dos ejercicios que nos ayudarán a comprender profundamente la programación orientada a objetos y sus aplicaciones prácticas. Comenzaremos con un sistema de reproducción multimedia y avanzaremos hacia un sistema de procesamiento de pagos.

### 4.1 Sistema de Reproducción de Medios (Nivel Básico)

**Contexto**:
Imagina que estás desarrollando un reproductor multimedia que debe manejar diferentes tipos de contenido (audio, video) de manera uniforme. Cada tipo de medio tiene sus características únicas, pero todos comparten funcionalidades básicas de reproducción.

**Objetivo Principal**:
Crear un sistema flexible y extensible para reproducir diferentes tipos de medios, aplicando los principios de abstracción y polimorfismo.

**Requisitos Detallados**:

1. **Clase Abstracta MediaPlayer**:
   - Atributos comunes:
     - Ruta del archivo
     - Estado de reproducción (playing/paused/stopped)
     - Posición actual de reproducción
     - Duración total del medio

   - Métodos abstractos requeridos:
     ```python
     @abstractmethod
     def play(self) -> str:
         """Inicia la reproducción del medio"""
         pass

     @abstractmethod
     def pause(self) -> str:
         """Pausa la reproducción actual"""
         pass

     @abstractmethod
     def stop(self) -> str:
         """Detiene la reproducción y reinicia la posición"""
         pass
     ```

2. **Implementaciones Específicas**:
   - AudioPlayer:
     - Manejo de calidad de audio
     - Control de volumen
     - Soporte para diferentes formatos (MP3, WAV)

   - VideoPlayer:
     - Control de resolución
     - Manejo de subtítulos
     - Soporte para diferentes formatos (MP4, AVI)

3. **Funcionalidades Adicionales**:
   - Mostrar tiempo de reproducción actual/total
   - Manejo de errores para archivos no soportados
   - Sistema de eventos para cambios de estado

### 4.2 Sistema de Procesamiento de Pagos (Nivel Intermedio)

**Contexto**:
Estás desarrollando el sistema de pagos para una plataforma de comercio electrónico. El sistema debe ser capaz de procesar pagos a través de diferentes métodos, manteniendo un alto nivel de seguridad y flexibilidad.

**Objetivo Principal**:
Implementar un sistema robusto y seguro que pueda manejar diferentes métodos de pago de manera consistente, con validaciones apropiadas y manejo de errores.

**Requisitos Detallados**:

1. **Clase Abstracta PaymentProcessor**:
   - Atributos comunes:
     - ID de transacción
     - Estado de la transacción
     - Historial de intentos
     - Configuración de seguridad

   - Métodos abstractos requeridos:
     ```python
     @abstractmethod
     def process_payment(self, amount: float, **kwargs) -> PaymentResult:
         """Procesa un pago con el método específico"""
         pass

     @abstractmethod
     def validate_payment_data(self, **kwargs) -> bool:
         """Valida los datos necesarios para el pago"""
         pass
     ```

2. **Implementaciones de Métodos de Pago**:
   - Tarjeta de Crédito:
     - Validación de número de tarjeta (algoritmo de Luhn)
     - Verificación de fecha de expiración
     - Validación de código CVV
     - Encriptación de datos sensibles

   - PayPal:
     - Autenticación OAuth
     - Manejo de tokens de acceso
     - Verificación de cuenta
     - Procesamiento de reembolsos

   - Criptomonedas:
     - Validación de dirección de wallet
     - Verificación de transacción en blockchain
     - Manejo de diferentes criptomonedas
     - Control de tasas de cambio

3. **Sistema de Resultados**:
   ```python
   @dataclass
   class PaymentResult:
       success: bool
       transaction_id: Optional[str]
       error_message: Optional[str]
       amount: float
       timestamp: datetime
   ```

4. **Validaciones Requeridas**:
   - Tarjeta de Crédito:
     - Formato: XXXX-XXXX-XXXX-XXXX
     - CVV: 3-4 dígitos
     - Fecha de expiración válida

   - PayPal:
     - Email válido
     - Token de autenticación
     - Estado de cuenta verificado

   - Criptomonedas:
     - Dirección de wallet válida
     - Tipo de criptomoneda soportado
     - Confirmaciones mínimas requeridas

## 5. Recursos Adicionales
- **Documentación oficial**: [Python ABC](https://docs.python.org/3/library/abc.html)
- **PEP 3119**: [Abstract Base Classes](https://www.python.org/dev/peps/pep-3119/)
- **Tutoriales recomendados**: Real Python - [Abstract Base Classes in Python](https://realpython.com/python-interface/)
- **El Libro De Python** - [Interfaces y Abstract Base Class (ABC)](https://ellibrodepython.com/abstract-base-class)

## 6. Soluciones Detalladas de Ejercicios

### 6.1 Sistema de Reproducción de Medios

Implementaremos un sistema de reproducción de medios que maneje diferentes tipos de contenido multimedia. Usaremos una clase abstracta como base y crearemos implementaciones específicas para cada tipo de medio.

```python
from abc import ABC, abstractmethod
from datetime import timedelta

class MediaPlayer(ABC):
    """
    Clase abstracta base para reproductores de medios.
    Define la interfaz común que todos los reproductores deben implementar.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.is_playing = False
        self.current_position = timedelta(0)
        self.duration = self._get_media_duration()

    @abstractmethod
    def _get_media_duration(self) -> timedelta:
        """
        Obtiene la duración del medio.
        Cada tipo de medio implementará su propia lógica.
        """
        pass

    @abstractmethod
    def play(self) -> str:
        """
        Inicia la reproducción del medio.
        """
        pass

    @abstractmethod
    def pause(self) -> str:
        """
        Pausa la reproducción del medio.
        """
        pass

    @abstractmethod
    def stop(self) -> str:
        """
        Detiene la reproducción y reinicia la posición.
        """
        pass

    def get_status(self) -> str:
        """
        Retorna el estado actual del reproductor.
        """
        status = "reproduciendo" if self.is_playing else "detenido"
        position = str(self.current_position).split('.')[0]  # Removemos microsegundos
        duration = str(self.duration).split('.')[0]
        return f"Estado: {status} | Posición: {position}/{duration}"

class AudioPlayer(MediaPlayer):
    """
    Implementación de reproductor de audio.
    Maneja formatos de audio como MP3, WAV, etc.
    """
    def __init__(self, file_path: str, audio_quality: str = "high"):
        self.audio_quality = audio_quality
        super().__init__(file_path)

    def _get_media_duration(self) -> timedelta:
        # Simulamos obtener duración del archivo de audio
        # En una implementación real, se leería del archivo
        return timedelta(minutes=3, seconds=30)

    def play(self) -> str:
        if not self.is_playing:
            self.is_playing = True
            return f"Reproduciendo audio en calidad {self.audio_quality}: {self.file_path}"
        return "El audio ya está en reproducción"

    def pause(self) -> str:
        if self.is_playing:
            self.is_playing = False
            return "Audio pausado"
        return "El audio ya está pausado"

    def stop(self) -> str:
        was_playing = self.is_playing
        self.is_playing = False
        self.current_position = timedelta(0)
        return "Audio detenido" if was_playing else "El audio ya estaba detenido"

class VideoPlayer(MediaPlayer):
    """
    Implementación de reproductor de video.
    Maneja formatos de video como MP4, AVI, etc.
    """
    def __init__(self, file_path: str, resolution: str = "1080p"):
        self.resolution = resolution
        self.subtitles_enabled = False
        super().__init__(file_path)

    def _get_media_duration(self) -> timedelta:
        # Simulamos obtener duración del archivo de video
        return timedelta(minutes=15, seconds=45)

    def play(self) -> str:
        if not self.is_playing:
            self.is_playing = True
            status = f"Reproduciendo video en {self.resolution}: {self.file_path}"
            if self.subtitles_enabled:
                status += " (con subtítulos)"
            return status
        return "El video ya está en reproducción"

    def pause(self) -> str:
        if self.is_playing:
            self.is_playing = False
            return "Video pausado"
        return "El video ya está pausado"

    def stop(self) -> str:
        was_playing = self.is_playing
        self.is_playing = False
        self.current_position = timedelta(0)
        return "Video detenido" if was_playing else "El video ya estaba detenido"

    def toggle_subtitles(self) -> str:
        """
        Activa o desactiva los subtítulos.
        Método específico para reproductor de video.
        """
        self.subtitles_enabled = not self.subtitles_enabled
        status = "activados" if self.subtitles_enabled else "desactivados"
        return f"Subtítulos {status}"

def demonstrate_media_player():
    """
    Función para demostrar el uso del sistema de reproducción.
    """
    print("=== Demo del Sistema de Reproducción ===")

    # Crear reproductores
    audio = AudioPlayer("music.mp3", "high")
    video = VideoPlayer("movie.mp4", "1080p")

    # Demostrar reproductor de audio
    print("\nPruebas con Audio:")
    print(audio.play())
    print(audio.get_status())
    print(audio.pause())
    print(audio.play())
    print(audio.stop())

    # Demostrar reproductor de video
    print("\nPruebas con Video:")
    print(video.play())
    print(video.get_status())
    print(video.toggle_subtitles())
    print(video.play())
    print(video.stop())

if __name__ == "__main__":
    demonstrate_media_player()
```

### 6.2 Sistema de Pagos

Este sistema implementa diferentes métodos de pago con sus validaciones y procesamientos específicos.

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict
import re

@dataclass
class PaymentResult:
    """
    Clase para estructurar el resultado de un pago.
    """
    success: bool
    transaction_id: Optional[str] = None
    error_message: Optional[str] = None
    amount: Optional[float] = None
    timestamp: datetime = datetime.now()

class PaymentProcessor(ABC):
    """
    Clase base abstracta para procesadores de pago.
    Define la interfaz común para todos los métodos de pago.
    """
    def __init__(self):
        self.transaction_history = []

    @abstractmethod
    def process_payment(self, amount: float, **kwargs) -> PaymentResult:
        """
        Procesa un pago con el método específico.
        Cada implementación definirá sus propios requisitos.
        """
        pass

    @abstractmethod
    def validate_payment_data(self, **kwargs) -> bool:
        """
        Valida los datos necesarios para el pago.
        """
        pass

    def record_transaction(self, result: PaymentResult) -> None:
        """
        Registra la transacción en el historial.
        """
        self.transaction_history.append({
            'timestamp': result.timestamp,
            'amount': result.amount,
            'success': result.success,
            'transaction_id': result.transaction_id,
            'error': result.error_message
        })

    def get_transaction_history(self) -> list:
        """
        Retorna el historial de transacciones.
        """
        return self.transaction_history

class CreditCardProcessor(PaymentProcessor):
    """
    Procesador de pagos con tarjeta de crédito.
    """
    def validate_payment_data(self, **kwargs) -> bool:
        required_fields = ['card_number', 'cvv', 'expiry_date']

        # Verificar campos requeridos
        if not all(field in kwargs for field in required_fields):
            return False

        # Validar número de tarjeta (simplificado)
        if not re.match(r'^\d{16}$', kwargs['card_number']):
            return False

        # Validar CVV
        if not re.match(r'^\d{3,4}$', kwargs['cvv']):
            return False

        # Validar fecha de expiración
        if not re.match(r'^\d{2}/\d{2}$', kwargs['expiry_date']):
            return False

        return True

    def process_payment(self, amount: float, **kwargs) -> PaymentResult:
        if not self.validate_payment_data(**kwargs):
            result = PaymentResult(
                success=False,
                error_message="Datos de tarjeta inválidos",
                amount=amount
            )
        else:
            # Simular procesamiento con banco
            result = PaymentResult(
                success=True,
                transaction_id=f"CC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                amount=amount
            )

        self.record_transaction(result)
        return result

class PayPalProcessor(PaymentProcessor):
    """
    Procesador de pagos con PayPal.
    """
    def validate_payment_data(self, **kwargs) -> bool:
        required_fields = ['email', 'paypal_token']

        # Verificar campos requeridos
        if not all(field in kwargs for field in required_fields):
            return False

        # Validar email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, kwargs['email']):
            return False

        # Validar token (simplificado)
        if len(kwargs['paypal_token']) < 10:
            return False

        return True

    def process_payment(self, amount: float, **kwargs) -> PaymentResult:
        if not self.validate_payment_data(**kwargs):
            result = PaymentResult(
                success=False,
                error_message="Datos de PayPal inválidos",
                amount=amount
            )
        else:
            # Simular procesamiento con PayPal
            result = PaymentResult(
                success=True,
                transaction_id=f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                amount=amount
            )

        self.record_transaction(result)
        return result

class CryptoProcessor(PaymentProcessor):
    """
    Procesador de pagos con criptomonedas.
    """
    def validate_payment_data(self, **kwargs) -> bool:
        required_fields = ['wallet_address', 'crypto_type']

        # Verificar campos requeridos
        if not all(field in kwargs for field in required_fields):
            return False

        # Validar dirección de wallet (simplificado)
        if len(kwargs['wallet_address']) < 26:
            return False

        # Validar tipo de cripto soportado
        supported_cryptos = ['BTC', 'ETH', 'USDT']
        if kwargs['crypto_type'] not in supported_cryptos:
            return False

        return True

    def process_payment(self, amount: float, **kwargs) -> PaymentResult:
        if not self.validate_payment_data(**kwargs):
            result = PaymentResult(
                success=False,
                error_message="Datos de crypto inválidos",
                amount=amount
            )
        else:
            # Simular procesamiento blockchain
            result = PaymentResult(
                success=True,
                transaction_id=f"CR-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                amount=amount
            )

        self.record_transaction(result)
        return result

def demonstrate_payment_system():
    """
    Función para demostrar el uso del sistema de pagos.
    """
    print("=== Demo del Sistema de Pagos ===")

    # Crear procesadores
    cc_processor = CreditCardProcessor()
    paypal_processor = PayPalProcessor()
    crypto_processor = CryptoProcessor()

    # Probar pago con tarjeta
    print("\nPrueba de Pago con Tarjeta:")
    cc_result = cc_processor.process_payment(
        amount=99.99,
        card_number="1234567890123456",
        cvv="123",
        expiry_date="12/25"
    )
    print(f"Resultado: {'Éxito' if cc_result.success else 'Error'}")
    print(f"ID Transacción: {cc_result.transaction_id}")

    # Probar pago con PayPal
    print("\nPrueba de Pago con PayPal:")
    pp_result = paypal_processor.process_payment(
        amount=50.00,
        email="user@example.com",
        paypal_token="token123456789"
    )
    print(f"Resultado: {'Éxito' if pp_result.success else 'Error'}")
    print(f"ID Transacción: {pp_result.transaction_id}")

    # Probar pago con Crypto
    print("\nPrueba de Pago con Crypto:")
    crypto_result = crypto_processor.process_payment(
        amount=1000.00,
        wallet_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        crypto_type="BTC"
    )
    print(f"Resultado: {'Éxito' if crypto_result.success else 'Error'}")
    print(f"ID Transacción: {crypto_result.transaction_id}")

if __name__ == "__main__":
    demonstrate_payment_system()
```

