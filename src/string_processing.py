class StringProcessing: 
    @staticmethod   
    def process_string(automaton, input_string):
        current_state = automaton.initial_state

        for symbol in input_string:
            next_state = automaton.get_next_state(current_state, symbol)
            if next_state is None:
                return False 
            current_state = next_state

        return current_state in automaton.acceptance_states