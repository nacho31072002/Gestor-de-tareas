import os

def clear_terminal ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu ():
    print('\n---Menú---')
    print('1. Listar tarea')
    print('2. Agregar tarea')
    print('3. Editar tarea')
    print('4. Tarea completada')
    print('5. Eliminar tarea')
    print('0. Salir')