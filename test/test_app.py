import unittest
from src.app import app
import json 
import os

# Clase para las pruebas de la aplicación
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

        # Crear un archivo de prueba para el autómata
        self.test_file = 'test_automaton.json'
        with open(self.test_file, 'w') as f:
            json.dump([{
                "id": "test1",
                "name": "Test Automaton",
                "initial_state": "q0",
                "acceptance_states": ["q0"],
                "alphabet": ["0", "1"],
                "states": ["q0", "q1"],
                "transitions": [
                    {"from_state": "q0", "symbol": "0", "to_state": "q0"},
                    {"from_state": "q0", "symbol": "1", "to_state": "q1"},
                    {"from_state": "q1", "symbol": "0", "to_state": "q0"},
                    {"from_state": "q1", "symbol": "1", "to_state": "q1"}
                ],
                "test_strings": ["0", "10"]
            }], f)

    # Función para limpiar después de las pruebas
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # Prueba de procesamiento del autómata
    def test_processing_automaton(self):
        with open(self.test_file, 'rb') as f:
            response = self.app.post(
                '/processing_automaton',
                data={'file': (f, self.test_file)},
                content_type = 'multipart/form-data'
            )

        # Verificar la respuesta
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(data[0]['id'], 'test1')