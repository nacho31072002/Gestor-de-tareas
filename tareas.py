from data import tareas


def listar_tarea ():
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
    pass

def completar_tarea ():
    pass

def eliminar_tarea ():
    pass