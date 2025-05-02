from src.config.constants import TAREAS_JSON_FILE
from src.helpers.file_helpers import read_json_file

def initialize_data () -> list[dict]:
    return read_json_file(TAREAS_JSON_FILE)
    
    
