from typing import Dict


class DataModel():
    def to_json(self) -> Dict:
        raise NotImplementedError('Implementa to_json en la clase hija')