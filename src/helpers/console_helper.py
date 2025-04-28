import os

from termcolor import colored

def clear_terminal ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu():
    print(colored('\n' + '='*30, 'cyan'))
    print(colored('     📝  Menú de Tareas  📝', 'yellow', attrs=['bold']))
    print(colored('='*30, 'cyan'))
    print(colored('1. Listar tarea', 'green'))
    print(colored('2. Agregar tarea', 'green'))
    print(colored('3. Editar tarea', 'green'))
    print(colored('4. Eliminar tarea', 'green'))
    print(colored('0. Salir', 'red'))
    print(colored('='*30, 'cyan'))