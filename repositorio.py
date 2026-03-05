import json
from pathlib import Path

from config import ARCHIVO_JSON
from ui import mensaje, pausar

# ───────────────────────────
# DATOS DE PRUEBA 
# ───────────────────────────

DATOS_PRUEBA = [
    {
        "id": 1, "nombre": "Empanada de Carne",
        "tipo": "Horneada", "emoji": "🥩",
        "relleno": "Carne molida, cebolla, huevo duro, aceitunas",
        "precio": 3500, "disponible": True,
    },
    {
        "id": 2, "nombre": "Empanada de Pollo",
        "tipo": "Horneada", "emoji": "🍗",
        "relleno": "Pollo desmenuzado, champiñones, crema de leche",
        "precio": 3200, "disponible": True,
    },
    {
        "id": 3, "nombre": "Empanada de Queso",
        "tipo": "Frita", "emoji": "🧀",
        "relleno": "Queso mozzarella, queso campesino, hierbas",
        "precio": 2800, "disponible": True,
    },
    {
        "id": 4, "nombre": "Empanada Hawaiana",
        "tipo": "Horneada", "emoji": "🍍",
        "relleno": "Jamón, piña, queso amarillo",
        "precio": 3000, "disponible": True,
    },
    {
        "id": 5, "nombre": "Empanada de Espinaca",
        "tipo": "Horneada", "emoji": "🥬",
        "relleno": "Espinaca, ricotta, ajo, nuez moscada",
        "precio": 2900, "disponible": False,
    },
    {
        "id": 6, "nombre": "Empanada Árabe",
        "tipo": "Horneada", "emoji": "🌿",
        "relleno": "Carne de cordero, cebolla, limón, especias",
        "precio": 4000, "disponible": True,
    },
]
