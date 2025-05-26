from src.helpers.console_helper import InputHelpers
from src.helpers.tarea_helpers import mostrar_menu
from src.controllers import tarea

def run ():
    ejecutar_menu()


def ejecutar_menu ():
    while True:
        print()
        mostrar_menu ()

        try:
            opcion = int(input('\nSeleccione una accion: ').strip())
        except ValueError:
            InputHelpers.clear_terminal()
            print('\nOpcion no valida.')
            continue
        
        InputHelpers.clear_terminal()

        if opcion == 1:
            tarea.listar_tarea()
        elif opcion == 2:
            tarea.agregar_tarea()
        elif opcion == 3:
            tarea.editar_tarea()
        elif opcion == 4:
            tarea.eliminar_tarea()
        elif opcion == 5:
            tarea.mostrar_tipo()
        elif opcion == 0:
            print('\nHasta luego!!')
            break
        else:
            print('\nIngrese un numero valido.')

       