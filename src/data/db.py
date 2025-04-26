from src.config.constants import COMPLETADA, PENDIENTE


def initialize_data () -> list[dict]:
    return [
        {
            'id' : 1, 
            'titulo' : 'Hacer ejercicio',
            'estado' : COMPLETADA
        },
        {
            'id' : 2, 
            'titulo' : 'Cortar pasto', 
            'estado' : PENDIENTE
        }
    ]