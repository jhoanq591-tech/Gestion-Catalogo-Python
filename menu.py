import sys

from config import C, ANCHO_UI, ARCHIVO_JSON
from ui import limpiar_pantalla, linea, confirmar


def mostrar_menu(catalogo: list[dict]) -> None:
    """
    Renderiza el menú principal con estadísticas en tiempo real
    y las 5 opciones disponibles.
    """
    limpiar_pantalla()

    total  = len(catalogo)
    dispon = sum(1 for e in catalogo if e["disponible"])

    # Cabecera
    print()
    linea("═")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.AMARILLO}{'🫓  LA EMPANADERA':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'Gestión de Catálogo':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'':^{ANCHO_UI}}{C.RESET}")
    linea("═")

    # Estadísticas rápidas
    print(
        f"\n  {C.DIM}Empanadas en catálogo: {C.BOLD}{C.AMARILLO}{total}{C.RESET}   "
        f"{C.DIM}Disponibles: {C.BOLD}{C.VERDE}{dispon}{C.RESET}\n"
    )

    # Opciones
    opciones = [
        ("1", "📋", "Listar empanadas",  C.CYAN),
        ("2", "➕", "Agregar empanada",  C.VERDE),
        ("3", "✏️ ", "Editar empanada",   C.AMARILLO),
        ("4", "🗑️ ", "Eliminar empanada", C.ROJO),
        ("5", "🚪", "Salir",             C.DIM),
    ]
    for num, ico, label, color in opciones:
        print(f"  {C.BOLD}{color}  {num}.{C.RESET}  {ico}  {label}")

    print()
    linea("─", color=C.DIM)


def pantalla_salida() -> None:
    """Muestra la pantalla de despedida y termina el proceso."""
    limpiar_pantalla()
    print()
    linea("═")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'🫓  ¡Hasta pronto!  🫓':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'La Empanadera — Catálogo':^{ANCHO_UI}}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{'':^{ANCHO_UI}}{C.RESET}")
    linea("═")
    print(f"\n  {C.DIM}Todos los cambios están guardados en '{ARCHIVO_JSON}'.{C.RESET}\n")
    sys.exit(0)


def pedir_opcion() -> str:
    """Lee y retorna la opción ingresada por el usuario."""
    return input(
        f"  {C.BOLD}{C.AMARILLO}▶  Selecciona una opción (1-5): {C.RESET}"
    ).strip()
