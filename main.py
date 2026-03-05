from repositorio import cargar_empanadas
from operaciones import (
    listar_empanadas,
    agregar_empanada,
    editar_empanada,
    eliminar_empanada,
)
from menu import mostrar_menu, pantalla_salida, pedir_opcion
from ui import mensaje, pausar


def main() -> None:
    """Bucle principal del programa."""
    catalogo = cargar_empanadas()

    while True:
        mostrar_menu(catalogo)
        opcion = pedir_opcion()

        if opcion == "1":
            listar_empanadas(catalogo)

        elif opcion == "2":
            catalogo = agregar_empanada(catalogo)

        elif opcion == "3":
            catalogo = editar_empanada(catalogo)

        elif opcion == "4":
            catalogo = eliminar_empanada(catalogo)

        elif opcion == "5":
            from ui import confirmar
            if confirmar("¿Seguro que deseas salir?"):
                pantalla_salida()

        else:
            mensaje("Opción inválida. Elige entre 1 y 5.", "error")
            pausar()


if __name__ == "__main__":
    main()