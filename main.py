from hellpers import clear_terminal, mostrar_menu

def run ():
    pass

if __name__ == '__main__':
    run ()


tareas = [{'id' : 1, 'titulo' : 'Hacer ejercicio', 'estado' : 'Completa'}]

def listar_tarea ():
    for tarea in tareas:
        print (f"{tarea['id']} - {tarea['titulo']} ({tarea['estado']})")


def agregar_tarea (): 
    agregar_id = int(input('Agregue el id: '))
    agregar_titulo = str(input('Agregue dicha tarea: '))
    agregar_estado = (input('Completada o pendiente: '))

    agregar_diccionario = {
        'id' : agregar_id,
        'titulo' : agregar_titulo,
        'estado' : agregar_estado
    }
    tareas.append(agregar_diccionario)


def ejecutar_menu ():
    while True:
        print()
        listar_tarea ()
        mostrar_menu ()
        
        opcion = int(input('\nSeleccione una accion: '))
        if opcion == 1:
            print('\nAgregando tarea...\n')
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