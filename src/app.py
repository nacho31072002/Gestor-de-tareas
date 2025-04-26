from src.helpers.console_helper import clear_terminal, mostrar_menu
from src.controllers.tarea_controller import listar_tarea, agregar_tarea, editar_tarea, eliminar_tarea

def run ():
    ejecutar_menu()


def ejecutar_menu ():
    while True:
        print()
        mostrar_menu ()

        try:
            opcion = int(input('\nSeleccione una accion: ').strip())
        except ValueError:
            clear_terminal()
            print('\nOpcion no valida.')
            continue
        
        clear_terminal()

        if opcion == 1:
            listar_tarea()
        elif opcion == 2:
            agregar_tarea()
        elif opcion == 3:
            editar_tarea()
        elif opcion == 4:
            eliminar_tarea()
        elif opcion == 0:
            print('\nHasta luego!!')
            break
        else:
            print('\nIngrese un numero valido.')

       