# Clase que representa un autómata
class Automaton: 
    # Funcion constructora
    def __init__(self, id, name, initial_state, acceptance_states, alphabet, states, transitions):
        self.id = id
        self.name = name 
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.transition_table = self.build_transition_table()

    # Funcion para construir la tabla de transiciones
    def build_transition_table(self):
        table = {}
        for transition in self.transitions:
            from_state = transition['from_state']
            symbol = transition['symbol']
            to_state = transition['to_state']

            if from_state not in table:
                table[from_state] = {}
            table[from_state][symbol] = to_state 
        return table

    # Funcion para obtener el siguiente estado
    def get_next_state(self, current_state, symbol):
        return self.transition_table.get(current_state, {}).get(symbol, None)