from termcolor import colored

from .file_helpers import write_json_file
from src.data import tareas_db
from src.config.constants import TAREAS_JSON_FILE

def mostrar_menu():
    print(colored('\n' + '='*30, 'cyan'))
    print(colored('     📝  Menú de Tareas  📝', 'yellow', attrs=['bold']))
    print(colored('='*30, 'cyan'))
    print(colored('1. Listar tarea', 'green'))
    print(colored('2. Agregar tarea', 'green'))
    print(colored('3. Editar tarea', 'green'))
    print(colored('4. Eliminar tarea', 'green'))
    print(colored('5. Listar tipo', 'green'))
    print(colored('0. Salir', 'red'))
    print(colored('='*30, 'cyan'))


def mostrar_tipo_tarea():
    print(colored('\n' + '='*30, 'cyan'))
    print(colored('  🗂️  Tipos de Tarea Disponibles  ', 'yellow', attrs=['bold']))
    print(colored('='*30, 'cyan'))
    print(colored('1. 📄 Tarea Normal', 'green'))
    print(colored('2. 🚨 Tarea Urgente', 'green'))
    print(colored('='*30, 'cyan'))

    tipo_opcion = input(colored("\nSeleccione una opción (1-2, por defecto 1): ")).strip()
    return tipo_opcion or "1"


def save_tareas():
    tarea_list: list[dict] = [tarea.to_dict() for tarea in tareas_db]
    write_json_file(TAREAS_JSON_FILE, tarea_list)

