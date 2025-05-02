from typing import Optional

from src.data import tareas_db
from src.config.constants import COMPLETADA, PENDIENTE
from src.helpers.console_helper import get_string, get_int, get_bool
from src.helpers.tarea_helpers import save_tareas


def listar_tarea () -> list[dict]:
    print('\nListando tareas...\n')
    if not __check_tareas():
        return

    for i, tareas in enumerate(tareas_db, start=1):
        print (f"{i} - {tareas['titulo']} ({tareas['estado']})")


def agregar_tarea ():
    print('\nAgregando tarea...\n')
    agregar_id = len(tareas_db) + 1
    agregar_titulo = get_string ('Agregue una tarea: ', accept_blank = False)
    estado_bool = get_bool ('Completada o Pendiente? C/P: ', accept_blank = False)
    agregar_estado = COMPLETADA if estado_bool else PENDIENTE

    agregar_diccionario = {
        'id' : agregar_id,
        'titulo' : agregar_titulo,
        'estado' : agregar_estado 
    }
    tareas_db.append(agregar_diccionario)
    save_tareas()


def editar_tarea ():
    print('\n Editando tareas...\n')
    if not __check_tareas():
        return
    listar_tarea()
    print()
    tarea_elegida = __find_tareas ()
    view_status = tarea_elegida['estado']
    tarea_elegida['titulo'] = get_string (f"Agregue un nuevo titulo ({tarea_elegida['titulo']}): ", accept_blank = True) or tarea_elegida['titulo'] 
    estado = get_bool(f"Completada o pendiente? C/P ({view_status}): ")
    if estado is not None:
        tarea_elegida['estado'] = COMPLETADA if estado else PENDIENTE
    save_tareas()  


def eliminar_tarea ():
    print('\nEliminado tarea...')
    if not __check_tareas():
        return
    listar_tarea()
    print()
    option = get_int (
        f'Elije una opcion (1 - {len(tareas_db)}): ', 
        accept_blank = True, 
        min_value = 1, 
        max_value = len(tareas_db)
    )
    if option is None:
        print('Operacion cancelada.')
    else:
        tarea_eliminada = tareas_db.pop(option - 1)
        print(f"\nTarea eliminada: {tarea_eliminada['titulo']} ({tarea_eliminada['estado']})")
    save_tareas()


def __check_tareas():
    if not tareas_db:
        print('No hay tareas cargadas.')
        return False
    return True

        
def __find_tareas() -> Optional[dict]:
    option = get_int(
        f'Elige una tarea (1 - {len(tareas_db)}): ',
        accept_blank = False, 
        min_value = 1, 
        max_value = len(tareas_db)
    ) 
    tareas = tareas_db[option - 1]
    print(f"\n{option} - {tareas['titulo']} ({tareas['estado']})")
    return tareas