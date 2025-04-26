from typing import Optional

from src.data.db import initialize_data
from src.config.constants import COMPLETADA, PENDIENTE

tarea = initialize_data()
def listar_tarea () -> list[dict]:
    print('\nListando tareas...\n')
    if not __check_tareas():
        return

    for i, tareas in enumerate(tarea, start=1):
        print (f"{i} - {tareas['titulo']} ({tareas['estado']})")


def agregar_tarea ():
    print('\nAgregando tarea...\n')
    agregar_id = len(tarea) + 1
    while True:
        try:
            agregar_titulo = str(input('Agregue dicha tarea: ').strip())
            if not agregar_titulo:
                raise ValueError('Error: Agregue un titulo.')
            break
        except ValueError as error:
            print(f'\n{error}') 


    while True:
        estado_input = str(input('Completada o Pendiente? C/P: ').upper())
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
    tarea.append(agregar_diccionario)

def editar_tarea ():
    print('\n Editando tareas...\n')
    if not __check_tareas():
        return
    listar_tarea()
    print()
    try:
        tarea_elegida = __find_tareas ()
        nuevo_titulo = input(f"Agregue un nuevo titulo ({tarea_elegida['titulo']}): ").strip()
        nuevo_estado = input(f"Completada o pendiente? C/P ({tarea_elegida['estado']}): ").strip()
        if nuevo_titulo:
            tarea_elegida['titulo'] = nuevo_titulo
        if nuevo_estado.strip().upper() == 'C':
            tarea_elegida['estado'] = nuevo_estado and COMPLETADA
        elif nuevo_estado.strip().upper() == 'P':
            tarea_elegida['estado'] = nuevo_estado and PENDIENTE        
    except TypeError:
        return editar_tarea()
    

def eliminar_tarea ():
    print('\nEliminado tarea...')
    if not __check_tareas():
        return
    listar_tarea()
    print()
    while True:
        try:
            option = int(input(f'Elije una opcion (1 - {len(tarea)}): ').strip())
            tarea_eliminada = tarea.pop(option - 1)
            print(f'\nTarea eliminada: {tarea_eliminada['titulo']} ({tarea_eliminada['estado']})')
            break
        except ValueError:
            print('\nError: Ingrese un numero')
        except IndexError:
            print(f'\nError: Ingrese un numero de (1 - {len(tarea)})')



def __check_tareas():
    if not tarea:
        print('No hay tareas cargadas: ')
        return False
    return True

        
def __find_tareas() -> Optional[dict]:
    try:
        option = int(input(f'Elige una tarea (1 - {len(tarea)}): ').strip())
        while option < 1 or option > len(tarea):
            print('Opción inválida. Intenta de nuevo.')
            option = int(input(f'Elige una tarea (1 - {len(tarea)}): ').strip()) 
        tareas = tarea[option - 1]
        print(f"\n{option} - {tareas['titulo']} ({tareas['estado']})")
        return tareas
    except ValueError:
        print('\nIngrese un numero\n')
        return __find_tareas()