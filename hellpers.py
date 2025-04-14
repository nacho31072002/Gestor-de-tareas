import os

def clear_terminal ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu ():
    print('\n---Menú---')
    print('1. Agregar tarea')
    print('2. Editar tarea')
    print('3. Tarea completada')
    print('4. Eliminar tarea')
    print('0. Salir')