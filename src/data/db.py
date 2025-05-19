from typing import List

from src.config.constants import TAREAS_JSON_FILE
from src.helpers.file_helpers import read_json_file
from .models.tarea_model import TareaModel

def initialize_data () -> List[TareaModel]:
    tarea_list: list[dict] = read_json_file(TAREAS_JSON_FILE)
    return [TareaModel(**tarea_dict) for tarea_dict in tarea_list]
    
    
