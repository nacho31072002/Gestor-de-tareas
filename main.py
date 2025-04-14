from hellpers import clear_terminal, mostrar_menu
from tareas import listar_tarea, agregar_tarea


def ejecutar_menu ():
    while True:
        print()
        listar_tarea ()
        mostrar_menu ()
        
        opcion = int(input('\nSeleccione una accion: '))
        clear_terminal ()
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            print('\nEditando tareas...')
        elif opcion == 3:
            print('\nCompletada o Incompleta: ')
        elif opcion == 4:
            print('\nEliminado tarea...')
        elif opcion == 0:
            print('\nHasta luego!!')
            break
        else:
            print('\nOpcion no valida')
        clear_terminal ()


ejecutar_menu()