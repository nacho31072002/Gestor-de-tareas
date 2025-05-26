from typing import Optional
from typing import List
from datetime import datetime

from src.data import tareas_db
from src.config.constants import COMPLETADA, PENDIENTE
from src.helpers.console_helper import InputHelpers
from src.helpers.tarea_helpers import save_tareas
from src.data.models.tarea_base import TareaBase
from src.data.models.tarea_urgente import TareaUrgente
from src.generators.tarea_generator import TareaGenerator
from src.helpers.tarea_helpers import mostrar_tipo_tarea


class TareaController:

    def listar_tarea(self) -> List[dict]:
        print('\nListando tareas...\n')
        if not self.__check_tareas():
            return

        for i, tareas in enumerate(tareas_db, start=1):
            print (f"{i} - {tareas.mostrar_info()}")
        
    def agregar_tarea(self):
        print('\nAgregando tarea...\n')
        id = len(tareas_db) + 1
        titulo = InputHelpers.get_string ('Agregue una tarea: ', accept_blank = False)

        tipo_opcion = mostrar_tipo_tarea()
        tipo_map = {"1": "normal", "2": "urgente"}
        tipo = tipo_map.get(tipo_opcion, "Normal")

        estado_bool = InputHelpers.get_bool ('Completada o Pendiente? C/P: ', accept_blank = False)
        estado = COMPLETADA if estado_bool else PENDIENTE

        kwargs = {}
        if tipo == "urgente":
            kwargs['fecha_limite'] = InputHelpers.pedir_fecha_limite()

        tarea = TareaGenerator.crear_tarea(tipo, id, titulo, estado, **kwargs)
        tareas_db.append(tarea)
        save_tareas()

    def editar_tarea(self):
        print('\n Editando tareas...\n')
        if not self.__check_tareas():
            return
        
        self.listar_tarea()
        print()

        tarea_elegida = self.__find_tareas()
        view_status = tarea_elegida.estado

        tarea_elegida.titulo = InputHelpers.get_string (f"Agregue un nuevo titulo ({tarea_elegida.titulo}): ", accept_blank = True) or tarea_elegida.titulo 
        estado = InputHelpers.get_bool(f"Completada o pendiente? C/P ({view_status}): ")

        if estado is not None:
            tarea_elegida.estado = COMPLETADA if estado else PENDIENTE

        if isinstance(tarea_elegida, TareaUrgente):
            fecha_actual = tarea_elegida.fecha_limite
            try:
                fecha_legible = datetime.fromisoformat(fecha_actual).strftime("%d/%m/%Y")
            except ValueError:
                fecha_legible = fecha_actual

            nueva_fecha = InputHelpers.pedir_fecha_limite(
                f"Fecha límite nueva ({fecha_legible}) [Enter para mantener]: "
            )
            if nueva_fecha != '':
                tarea_elegida.fecha_limite = nueva_fecha

        save_tareas()  

    def eliminar_tarea(self):
        print('\nEliminado tarea...')
        if not self.__check_tareas():
            return
        self.listar_tarea()
        print()
        option = InputHelpers.get_int (
            f'Elije una opcion (1 - {len(tareas_db)}) [Enter para cancelar]: ', 
            accept_blank = True, 
            min_value = 1, 
            max_value = len(tareas_db)
        )
        if option is None:
            print('\nOperacion cancelada.')
        else:
            tarea_eliminada = tareas_db.pop(option - 1)
            print(f"\nTarea eliminada: {tarea_eliminada.titulo} ({tarea_eliminada.estado})")
        save_tareas()

    def mostrar_tipo(self):
        print("\nTareas agrupadas por tipo...\n")
        if not self.__check_tareas():
            return
        
        tipos = {}
        for tarea in tareas_db:
            tipo = tarea.get_tipo()
            if tipo not in tipos:
                tipos[tipo] = []
            tipos[tipo].append(tarea)
        
        for tipo, tareas in tipos.items():
            print(f"\n=== {tipo.upper()} ===")
            for tarea in tareas:
                print(f"  {tarea.mostrar_info()}")

    def __check_tareas(self):
        if not tareas_db:
            print('No hay tareas cargadas.')
            return False
        return True
            
    def __find_tareas(self) -> Optional[TareaBase]:
        option = InputHelpers.get_int(
        f'Elige una tarea (1 - {len(tareas_db)}): ',
            accept_blank = False, 
            min_value = 1, 
            max_value = len(tareas_db)
        ) 
        tareas = tareas_db[option - 1]
        print(f"\n{option} - {tareas.titulo} ({tareas.estado})")
        return tareas