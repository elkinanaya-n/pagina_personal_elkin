# EJERCICIO 1 

## Requerimientos Funcionales
###Interfaz Limpia: Los usuarios deben poder importar las funciones directamente desde el paquete:
from mini_turtle import adelante, abajo, reiniciar
Nueva Funcionalidad: Añadir una función reiniciar() que resetee la posicion_x a 0.

Estructura de Archivos:

mini_turtle_task/
├── mini_turtle/
│   ├── __init__.py
│   └── drawer_logic.py
├── main.py
└── README.md


##📝 Pasos de Implementación

1.Módulo de Lógica (drawer_logic.py): Mueve las funciones y la variable global aquí. Implementa reiniciar() usando global posicion_x.


## mini_turtle/drawer_logic.py

## Variable de estado global para simular la posición de la tortuga
## Se inicializa en 0, como requiere la nueva función reiniciar()
posicion_x = 0

def adelante():
    """Mueve la tortuga 'adelante' (incrementa la posición X)."""
    global posicion_x
    posicion_x += 1
    print(f"La tortuga avanza. Posición X: {posicion_x}")

def abajo():
    """Mueve la tortuga 'abajo' (simula un movimiento vertical)."""
  Esta función no afecta a posicion_x en este ejemplo 
  pero simula una acción del dibujante.
    print(f"La tortuga baja. Posición X se mantiene en: {posicion_x}")

def reiniciar():
    """
    Resetea el estado de la tortuga, estableciendo posicion_x a 0.
    Requerimiento Funcional Nuevo.
    """
    global posicion_x
    posicion_x = 0
    print("El dibujo ha sido reiniciado. Posición X: 0")

2.Interfaz (__init__.py)

##Este archivo expone las funciones públicas de tu módulo de lógica para que los usuarios puedan importarlas directamente desde el paquete 
(mini_turtle).

# mini_turtle/__init__.py

# Importa las funciones que quieres exponer desde el módulo de lógica
from .drawer_logic import adelante, abajo, reiniciar

# Define __all__ para especificar explícitamente qué nombres se exponen 
# cuando un usuario hace 'from mini_turtle import *'
__all__ = [
    "adelante", 
    "abajo", 
    "reiniciar"
]


3. Prueba (main.py)

##Este es el script de prueba del usuario que importa y utiliza las funciones para dibujar una "escalera", reinicia y luego dibuja algo nuevo.

# main.py

## Interfaz Limpia: Importar las funciones directamente desde el paquete
from mini_turtle import adelante, abajo, reiniciar

print("--- 🎨 Inicio del Dibujo (Escalera) ---")

## Dibuja una escalera (Ejemplo)
adelante()
abajo()
adelante()
abajo()
adelante()

print("\n--- 🔄 Reiniciando el Dibujo ---")
## Usa la nueva función reiniciar()
reiniciar()

print("\n--- 🖌️ Dibujando algo nuevo ---")
## Dibuja algo nuevo desde la posición inicial (0)
abajo()
adelante()
adelante()
abajo()

print("--- ✅ Fin del Script ---")



