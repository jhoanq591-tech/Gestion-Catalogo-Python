
# ╔══════════════════════════════════════════════╗
# ║  Utilidades de interfaz de consola           ║
# ╚══════════════════════════════════════════════╝

import os
from config import C, ANCHO_UI


# ──────────────────────────────────────────────
# PANTALLA
# ──────────────────────────────────────────────

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input(f"\n  {C.DIM}Presiona Enter para continuar…{C.RESET}")


# ──────────────────────────────────────────────
# ELEMENTOS VISUALES
# ──────────────────────────────────────────────

def linea(caracter="─", ancho=ANCHO_UI, color=C.AMARILLO):
    print(f"{color}{caracter * ancho}{C.RESET}")


def titulo_bloque(texto, icono="🫓"):
    print()
    linea("═")
    print(f"{C.BG_MARRON}{C.BOLD}{C.NEGRO}{'█' * ANCHO_UI}{C.RESET}")
    linea_txt = f"  {icono}  {texto}  "
    esp = " " * ((ANCHO_UI - len(linea_txt)) // 2)
    print(f"{C.BG_MARRON}{C.BOLD}{C.BLANCO}{esp}{linea_txt}{esp}{C.RESET}")
    print(f"{C.BG_MARRON}{C.BOLD}{C.NEGRO}{'█' * ANCHO_UI}{C.RESET}")
    linea("═")
    print()


def mensaje(texto, tipo="info"):
    iconos = {
        "ok":    "✅",
        "error": "❌",
        "warn":  "⚠️ ",
        "info":  "ℹ️ ",
        "tip":   "💡",
    }
    colores = {
        "ok":    C.VERDE,
        "error": C.ROJO,
        "warn":  C.AMARILLO,
        "info":  C.CYAN,
        "tip":   C.MAGENTA,
    }
    icono = iconos.get(tipo, "•")
    color = colores.get(tipo, C.BLANCO)
    print(f"\n  {color}{C.BOLD}{icono}  {texto}{C.RESET}\n")


def mostrar_detalle(emp):
    estado = (
        f"{C.VERDE}Disponible{C.RESET}"
        if emp["disponible"]
        else f"{C.ROJO}Agotada{C.RESET}"
    )
    print(f"\n    {emp['emoji']}  {C.BOLD}{emp['nombre']}{C.RESET}")
    print(f"    {C.DIM}ID:{C.RESET}          {emp['id']}")
    print(f"    {C.DIM}Tipo:{C.RESET}        {emp['tipo']}")
    print(f"    {C.DIM}Relleno:{C.RESET}     {emp['relleno']}")
    print(f"    {C.DIM}Precio:{C.RESET}      {C.CYAN}${emp['precio']:,.0f}{C.RESET}")
    print(f"    {C.DIM}Estado:{C.RESET}      {estado}\n")


# ──────────────────────────────────────────────
# ENTRADAS DE USUARIO
# ──────────────────────────────────────────────

def pedir_input(prompt, obligatorio=True):
    while True:
        valor = input(f"  {C.CYAN}▶  {prompt}: {C.RESET}").strip()
        if valor or not obligatorio:
            return valor
        print(f"  {C.ROJO}Este campo es obligatorio.{C.RESET}")


def pedir_int(prompt, minimo=0):

    while True:
        raw = input(f"  {C.CYAN}▶  {prompt}: {C.RESET}").strip()
        try:
            valor = int(raw)
            if valor >= minimo:
                return valor
            print(f"  {C.ROJO}Debe ser mayor o igual a {minimo}.{C.RESET}")
        except ValueError:
            print(f"  {C.ROJO}Ingresa un número válido.{C.RESET}")


def pedir_bool(prompt):
 
    while True:
        raw = input(f"  {C.CYAN}▶  {prompt} (s/n): {C.RESET}").strip().lower()
        if raw in ("s", "si", "sí", "y", "yes", "1"):
            return True
        if raw in ("n", "no", "0"):
            return False
        print(f"  {C.ROJO}Responde 's' o 'n'.{C.RESET}")


def confirmar(pregunta):
   
    return pedir_bool(pregunta)


def elegir_tipo():

    tipos = ["Horneada", "Frita", "Al vapor"]
    print(f"\n  {C.DIM}Selecciona el tipo de cocción:{C.RESET}")
    for i, t in enumerate(tipos, 1):
        print(f"    {C.AMARILLO}{i}.{C.RESET} {t}")
    while True:
        raw = input(f"  {C.CYAN}▶  Opción (1-{len(tipos)}): {C.RESET}").strip()
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(tipos):
                return tipos[idx]
        except ValueError:
            pass
        print(f"  {C.ROJO}Opción inválida.{C.RESET}")
