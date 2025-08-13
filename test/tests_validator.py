import unittest
from src.validator import AutomatonValidator

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

    def test_validator_autonomo(self):
        errors = AutomatonValidator.validate(self.valid_automaton)
        self.assertEqual(errors, [])

    def test_missing_initial_state(self):
        invalid_automaton = self.valid_automaton.copy()
        invalid_automaton['initial_state'] = 'q3'
        errors = AutomatonValidator.validate(invalid_automaton)
        self.assertTrue(len(errors) > 0)
        self.assertIn("not found in states list", errors[0])