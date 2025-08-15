import unittest
from src.validator import AutomatonValidator

# Clase para las pruebas del validador
class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid_automaton = {
            'id': 'valid1',
            'name': 'Valid Automaton',
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

    # Prueba de validación del autómata
    def test_validator_automaton(self):
        errors = AutomatonValidator.validate(self.valid_automaton)
        self.assertEqual(errors, [])

    # Prueba de estado inicial faltante
    def test_missing_initial_state(self):
        invalid_automaton = self.valid_automaton.copy()
        invalid_automaton['initial_state'] = 'q3'
        errors = AutomatonValidator.validate(invalid_automaton)
        self.assertTrue(len(errors) > 0)
        self.assertIn("not found in states list", errors[0])