from hellpers import clear_terminal, mostrar_menu
from tareas import listar_tarea, agregar_tarea, editar_tarea, eliminar_tarea

def run ():
    pass

if __name__ == '__main__':
    run ()


def ejecutar_menu ():
    while True:
        print()
        mostrar_menu ()
        
        opcion = int(input('\nSeleccione una accion: '))
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
            clear_terminal()
            break
        else:
            print('\nOpcion no valida')
        


ejecutar_menu()