from data import tareas


def listar_tarea ():
    print('\nListando tareas...\n')
    if not __check_tareas():
        return

    for tarea in tareas:
        print (f"{tarea['id']} - {tarea['titulo']} ({tarea['estado']})")


def agregar_tarea ():
    print('\nAgregando tarea...\n')
    agregar_id = int(input('Agregue el id: '))
    agregar_titulo = str(input('Agregue dicha tarea: '))
    agregar_estado = (input('Completada o Pendiente: '))

    agregar_diccionario = {
        'id' : agregar_id,
        'titulo' : agregar_titulo,
        'estado' : agregar_estado
    }
    tareas.append(agregar_diccionario)

def editar_tarea ():
     print('\n Editando tareas...\n')
     if not __check_tareas():
        return
     __find_tareas()

def completar_tarea ():
     if not __check_tareas():
        return

def eliminar_tarea ():
     if not __check_tareas():
        return

def __check_tareas():
    if not tareas:
        print('No hay tareas cargadas: ')
        return False
    return True

        
def __find_tareas() -> dict:
    option = int(input(f'Elige una tarea (1 - {len(tareas)}): '))
    while option < 1 or option > len(tareas):
        print('Opción inválida. Intenta de nuevo.')
        option = int(input(f'Elige una tarea (1 - {len(tareas)}): '))   
    for tarea in tareas:
        if option == tarea['id']:
            print(f"\n{tarea['id']} - {tarea['titulo']} ({tarea['estado']})")
            return tarea