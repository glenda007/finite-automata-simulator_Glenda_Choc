import unittest
from src.automaton import Automaton 

# Clase para las pruebas del autómata
class TestAutomaton(unittest.TestCase):
    def setUp(self):
        self.sample_automaton = {
            'id': 'test1',
            'name': 'Test Automaton',
            'initial_state': 'q0',
            'acceptance_states': ['q0'],
            'alphabet': ['0', '1'],
            'states': ['q0', 'q1'],
            'transitions': [
                {'from_state': 'q0', 'symbol': '0', 'to_state': 'q0'},
                {'from_state': 'q0', 'symbol': '1', 'to_state': 'q1'},
                {'from_state': 'q1', 'symbol': '0', 'to_state': 'q0'},
                {'from_state': 'q1', 'symbol': '1', 'to_state': 'q1'}
            ]
        }

    # Prueba de creación del autómata
    def test_automaton_creation(self):
        automaton = Automaton(**self.sample_automaton)
        self.assertEqual(automaton.id, 'test1')
        self.assertEqual(automaton.initial_state, 'q0')

    # Prueba de la tabla de transiciones
    def test_transition_table(self):
        automaton = Automaton(**self.sample_automaton)
        self.assertEqual(automaton.get_next_state('q0', '0'), 'q0')
        self.assertEqual(automaton.get_next_state('q0', '1'), 'q1')
        self.assertIsNone(automaton.get_next_state('q1', '2'))  