import json
from pathlib import Path

from config import ARCHIVO_JSON
from ui import mensaje, pausar

# ─────────────────────────────
# DATOS DE PRUEBA 
# ─────────────────────────────

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


# ──────────────────────────────────────────────
# FUNCIONES PÚBLICAS
# ──────────────────────────────────────────────

def cargar_empanadas() -> list[dict]:

    ruta = Path(ARCHIVO_JSON)
    if not ruta.exists():
        guardar_empanadas(DATOS_PRUEBA)
        mensaje(f"Archivo '{ARCHIVO_JSON}' creado con datos de prueba.", "ok")
        pausar()
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_empanadas(catalogo: list[dict]) -> None:
  
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=2)


def siguiente_id(catalogo: list[dict]) -> int:
    return max((e["id"] for e in catalogo), default=0) + 1


def buscar_por_id(catalogo: list[dict], id_buscado: int) -> dict | None:
    return next((e for e in catalogo if e["id"] == id_buscado), None)
