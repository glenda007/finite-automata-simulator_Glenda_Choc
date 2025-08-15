# Clase para el procesamiento de cadenas
class StringProcessing: 
    @staticmethod   
    def process_string(automaton, input_string):
        current_state = automaton.initial_state

        # Procesar cada símbolo de la cadena de entrada
        for symbol in input_string:
            next_state = automaton.get_next_state(current_state, symbol)
            if next_state is None:
                return False 
            current_state = next_state

        # Verificar si el estado final es un estado de aceptación
        return current_state in automaton.acceptance_states