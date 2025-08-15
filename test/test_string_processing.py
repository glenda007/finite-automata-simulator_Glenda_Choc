import unittest
from src.string_processing import StringProcessing
from src.automaton import Automaton

# Clase para las pruebas del procesamiento de cadenas
class TestStringProcessing(unittest.TestCase):
    def setUp(self):
        self.even_zeros_automaton = Automaton (
            id = 'test1',
            name = 'Even zeros',
            initial_state = 'q0',
            acceptance_states = ['q0'],
            alphabet = ['0', '1'],
            states = ['q0', 'q1'],
            transitions = [
                {'from_state': 'q0', 'symbol': '0', 'to_state': 'q1'},
                {'from_state': 'q0', 'symbol': '1', 'to_state': 'q0'},
                {'from_state': 'q1', 'symbol': '0', 'to_state': 'q0'},
                {'from_state': 'q1', 'symbol': '1', 'to_state': 'q1'}
            ]
        ) 

    # Prueba de procesamiento de cadenas
    def test_string_processing(self):
        self.assertTrue(StringProcessing.process_string(self.even_zeros_automaton, "1001"))
        self.assertFalse(StringProcessing.process_string(self.even_zeros_automaton, "100"))