from typing import List

from src.config.constants import TAREAS_JSON_FILE
from src.helpers.file_helpers import read_json_file
from .models.tarea_base import TareaBase
from .models.tarea_factory import tarea_from_dict

def initialize_data() -> List[TareaBase]:
    tarea_list: List[dict] = read_json_file(TAREAS_JSON_FILE)
    return [tarea_from_dict(tarea_dict) for tarea_dict in tarea_list]
    
    
