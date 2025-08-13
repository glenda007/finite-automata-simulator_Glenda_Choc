from graphviz import Digraph
import os 
from datetime import datetime

class DiagramGenerator:
    @staticmethod
    def generate_diagram(automaton, output_dir='generate_diagrams'):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"automaton_{automaton.id}_{timestamp}"
        filepath = os.path.join(output_dir, filename)

        dot = Digraph(comment=automaton.name)
        dot.attr(rankdir='LR')

        for state in automaton.states:
            if state in automaton.acceptance_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)

            if state == automaton.initial_state:
                dot.node('start', shape='point')
                dot.edge('start', state)

        for transition in automaton.transitions:
            dot.edge(transition['from_state'],
                    transition['to_state'],
                    label=transition['symbol'])
            
        output_path = dot.render(filepath, format='png', cleanup=True)
        return output_path