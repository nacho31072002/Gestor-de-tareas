from typing import Optional

from src.data import tareas
from src.constants import COMPLETADA, PENDIENTE


def listar_tarea ():
    print('\nListando tareas...\n')
    if not __check_tareas():
        return

    for i, tarea in enumerate(tareas, start=1):
        print (f"{i} - {tarea['titulo']} ({tarea['estado']})")


def agregar_tarea ():
    print('\nAgregando tarea...\n')
    agregar_id = len(tareas), + 1
    agregar_titulo = str(input('Agregue dicha tarea: '))

    while True:
        estado_input = str(input('Completada o Pendiente? C/P: ')).strip().upper()
        if estado_input == 'C':
            agregar_estado = COMPLETADA
            break
        elif estado_input == 'P':
            agregar_estado = PENDIENTE 
            break
        else:
            print('Opcion invalida. Intentalo de nuevo')

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
     tarea = __find_tareas ()
     nuevo_titulo = input(f"Agregue un nuevo titulo ({tarea['titulo']}): ")
     nuevo_estado = input(f"Completada o pendiente? C/P ({tarea['estado']}): ")
     if nuevo_titulo:
         tarea['titulo'] = nuevo_titulo
     if nuevo_estado.strip().upper() == 'C':
         tarea['estado'] = nuevo_estado and COMPLETADA
     elif nuevo_estado.strip().upper() == 'P':
         tarea['estado'] = nuevo_estado and PENDIENTE        


def eliminar_tarea ():
     print('\nEliminado tarea...')
     if not __check_tareas():
        return
     listar_tarea()
     print()
     option = int(input(f'Elije una opcion (1 - {len(tareas)}): '))
     tarea_eliminada = tareas.pop(option - 1)
     print(f'\nTarea eliminada: {tarea_eliminada['titulo']} ({tarea_eliminada['estado']})')



def __check_tareas():
    if not tareas:
        print('No hay tareas cargadas: ')
        return False
    return True

        
def __find_tareas() -> Optional[dict]:
    option = int(input(f'Elige una tarea (1 - {len(tareas)}): '))
    while option < 1 or option > len(tareas):
        print('Opción inválida. Intenta de nuevo.')
        option = int(input(f'Elige una tarea (1 - {len(tareas)}): '))   
    tarea = tareas[option - 1]
    print(f"\n{option} - {tarea['titulo']} ({tarea['estado']})")
    return tarea