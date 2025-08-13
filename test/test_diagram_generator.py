import unittest
import os 
from src.diagram_generator import DiagramGenerator
from src.automaton import Automaton

class TestDiagram(unittest.TestCase):
    def test_diagram_generator(self):
        sample_automaton = {
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
        
        automaton = Automaton(**sample_automaton)
        path = DiagramGenerator.generate_diagram(automaton)

        self.assertTrue(os.path.exists(path))
        os.remove(path)