# ╔══════════════════════════════════════════════
#   Lógica CRUD del catálogo                     ║
# ╚══════════════════════════════════════════════╝

from config import C
from ui import (
    limpiar_pantalla, pausar, linea, titulo_bloque,
    mensaje, mostrar_detalle,
    pedir_input, pedir_int, pedir_bool, confirmar, elegir_tipo,
)
from repositorio import (
    cargar_empanadas, guardar_empanadas,
    siguiente_id, buscar_por_id,
)


# ══════════════════════════════════════════════
# 1. LISTAR EMPANADAS
# ══════════════════════════════════════════════

def listar_empanadas(catalogo: list[dict]) -> None:
 
    limpiar_pantalla()
    titulo_bloque("Catálogo de Empanadas", "📋")

    if not catalogo:
        mensaje("El catálogo está vacío. ¡Agrega tu primera empanada!", "warn")
        pausar()
        return


    total  = len(catalogo)
    dispon = sum(1 for e in catalogo if e["disponible"])
    avg_p  = sum(e["precio"] for e in catalogo) // total

    print(
        f"  {C.DIM}Total: {C.BOLD}{C.AMARILLO}{total}{C.RESET}  "
        f"{C.DIM}│ Disponibles: {C.BOLD}{C.VERDE}{dispon}{C.RESET}  "
        f"{C.DIM}│ Precio promedio: {C.BOLD}{C.CYAN}${avg_p:,.0f}{C.RESET}\n"
    )
    linea()

    for emp in catalogo:
        estado_color = C.VERDE if emp["disponible"] else C.ROJO
        estado_texto = "DISPONIBLE" if emp["disponible"] else "AGOTADA  "
        badge = f"{estado_color}{C.BOLD}[{estado_texto}]{C.RESET}"

        print(
            f"  {C.BOLD}{C.AMARILLO}#{emp['id']:02d}{C.RESET}  "
            f"{emp['emoji']}  "
            f"{C.BOLD}{C.BLANCO}{emp['nombre']:<26}{C.RESET}  "
            f"{badge}  "
            f"{C.CYAN}${emp['precio']:>6,.0f}{C.RESET}"
        )
        print(
            f"       {C.DIM}Tipo:{C.RESET} {C.MAGENTA}{emp['tipo']:<10}{C.RESET}  "
            f"{C.DIM}Relleno:{C.RESET} {emp['relleno'][:45]}"
        )
        linea("·", color=C.DIM)

    pausar()


# ══════════════════════════════════════════════
# 2. AGREGAR EMPANADA
# ══════════════════════════════════════════════

def agregar_empanada(catalogo: list[dict]) -> list[dict]:
  
    limpiar_pantalla()
    titulo_bloque("Agregar Nueva Empanada", "➕")
    print(f"  {C.DIM}Completa los datos de la nueva empanada:{C.RESET}\n")

    nombre     = pedir_input("Nombre de la empanada")
    emoji      = pedir_input("Emoji (ej: 🥩)", obligatorio=False) or "🥟"
    tipo       = elegir_tipo()
    relleno    = pedir_input("Relleno / ingredientes")
    precio     = pedir_int("Precio (COP $)", minimo=1)
    disponible = pedir_bool("¿Está disponible?")

    nueva = {
        "id":         siguiente_id(catalogo),
        "nombre":     nombre,
        "emoji":      emoji,
        "tipo":       tipo,
        "relleno":    relleno,
        "precio":     precio,
        "disponible": disponible,
    }

    linea()
    print(f"  {C.BOLD}Resumen de la nueva empanada:{C.RESET}")
    mostrar_detalle(nueva)
    linea()

    if confirmar("¿Guardar esta empanada?"):
        catalogo.append(nueva)
        guardar_empanadas(catalogo)
        mensaje(f"'{nombre}' agregada exitosamente al catálogo.", "ok")
    else:
        mensaje("Operación cancelada.", "warn")

    pausar()
    return catalogo


# ══════════════════════════════════════════════
# 3. EDITAR EMPANADA
# ══════════════════════════════════════════════

def editar_empanada(catalogo: list[dict]) -> list[dict]:

    limpiar_pantalla()
    titulo_bloque("Editar Empanada", "✏️")

    if not catalogo:
        mensaje("El catálogo está vacío.", "warn")
        pausar()
        return catalogo

   
    for emp in catalogo:
        print(f"  {C.AMARILLO}#{emp['id']:02d}{C.RESET}  {emp['emoji']}  {emp['nombre']}")
    linea()

    emp = _seleccionar_empanada(catalogo, "editar")
    if emp is None:
        return catalogo

    print(f"\n  {C.DIM}Datos actuales (Enter para conservar el valor):{C.RESET}\n")

    nuevo_nombre  = input(f"  {C.CYAN}▶  Nombre [{emp['nombre']}]: {C.RESET}").strip() or emp["nombre"]
    nuevo_emoji   = input(f"  {C.CYAN}▶  Emoji  [{emp['emoji']}]: {C.RESET}").strip()  or emp["emoji"]

    print(f"  {C.CYAN}▶  Tipo actual: {emp['tipo']} — ¿Cambiar? {C.RESET}", end="")
    nuevo_tipo = elegir_tipo() if input("(s/n): ").strip().lower() == "s" else emp["tipo"]

    nuevo_relleno = input(f"  {C.CYAN}▶  Relleno [{emp['relleno'][:40]}…]: {C.RESET}").strip() or emp["relleno"]

    raw_precio    = input(f"  {C.CYAN}▶  Precio [${emp['precio']:,.0f}]: {C.RESET}").strip()
    nuevo_precio  = int(raw_precio) if raw_precio.isdigit() else emp["precio"]

    print(f"  {C.CYAN}▶  Disponible actual: {'Sí' if emp['disponible'] else 'No'} — ¿Cambiar? {C.RESET}", end="")
    nueva_disp = (not emp["disponible"]) if input("(s/n): ").strip().lower() == "s" else emp["disponible"]

    emp.update({
        "nombre":     nuevo_nombre,
        "emoji":      nuevo_emoji,
        "tipo":       nuevo_tipo,
        "relleno":    nuevo_relleno,
        "precio":     nuevo_precio,
        "disponible": nueva_disp,
    })

    linea()
    print(f"  {C.BOLD}Datos actualizados:{C.RESET}")
    mostrar_detalle(emp)
    linea()

    if confirmar("¿Guardar los cambios?"):
        guardar_empanadas(catalogo)
        mensaje(f"'{emp['nombre']}' actualizada correctamente.", "ok")
    else:
        catalogo = cargar_empanadas()
        mensaje("Cambios descartados.", "warn")

    pausar()
    return catalogo
# ══════════════════════════════════════════════
# 4. ELIMINAR EMPANADA
# ══════════════════════════════════════════════

def eliminar_empanada(catalogo: list[dict]) -> list[dict]:
    limpiar_pantalla()
    titulo_bloque("Eliminar Empanada", "🗑️")

    if not catalogo:
        mensaje("El catálogo está vacío.", "warn")
        pausar()
        return catalogo

    for emp in catalogo:
        estado = f"{C.VERDE}✔{C.RESET}" if emp["disponible"] else f"{C.ROJO}✘{C.RESET}"
        print(f"  {C.AMARILLO}#{emp['id']:02d}{C.RESET}  {emp['emoji']}  {emp['nombre']:<28} {estado}")
    linea()

    emp = _seleccionar_empanada(catalogo, "eliminar")
    if emp is None:
        return catalogo

    print(f"\n  {C.BOLD}{C.ROJO}¿Eliminar permanentemente?{C.RESET}")
    mostrar_detalle(emp)

    if confirmar(f"Confirmar eliminación de '{emp['nombre']}'"):
        catalogo = [e for e in catalogo if e["id"] != emp["id"]]
        guardar_empanadas(catalogo)
        mensaje(f"'{emp['nombre']}' eliminada del catálogo.", "ok")
    else:
        mensaje("Eliminación cancelada.", "warn")

    pausar()
    return catalogo

# ══════════════════════════════════════════════
# HELPER PRIVADO
# ═══════════════════════════════════════════
def _seleccionar_empanada(catalogo: list[dict], accion: str) -> dict | None:
   
    while True:
        raw = input(
            f"  {C.CYAN}▶  ID de la empanada a {accion} (0 para cancelar): {C.RESET}"
        ).strip()
        try:
            id_sel = int(raw)
            if id_sel == 0:
                mensaje("Operación cancelada.", "warn")
                pausar()
                return None
            emp = buscar_por_id(catalogo, id_sel)
            if emp:
                return emp
            print(f"  {C.ROJO}ID no encontrado. Intenta de nuevo.{C.RESET}")
        except ValueError:
            print(f"  {C.ROJO}Ingresa un número válido.{C.RESET}")
            #holaaa
