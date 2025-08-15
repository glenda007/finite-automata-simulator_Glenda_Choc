# Clase para validar autómatas
class AutomatonValidator:
    @staticmethod
    # Funcion para validar los datos del autómata
    def validate(automaton_data):
        errors = []
        required_attributes = ['id', 'name', 'initial_state', 'acceptance_states', 'alphabet', 'states', 'transitions']
        # Verificar si faltan atributos requeridos
        for field in required_attributes:
            if field not in automaton_data:
                errors.append(f"Missing required field: {field}")

        # Verificar que no haya errores
        if errors:
            return errors

        # Verificar estados y transiciones
        states = automaton_data['states']
        initial_state = automaton_data['initial_state']
        acceptance_states = automaton_data['acceptance_states']

        if initial_state not in states:
            errors.append(f"Initial state '{initial_state}' not found in states list")

        for state in acceptance_states: 
            if state not in states:
                errors.append(f"Acceptance state '{state}' not found in states list")

        # Verificar transiciones
        alphabet = automaton_data['alphabet']
        for transition in automaton_data['transitions']:
            if transition['from_state'] not in states:
                errors.append(f"Transition from undefined state '{transition['from_state']}'")
            if transition['to_state'] not in states:
                errors.append(f"Transition to undefined state '{transition['to_state']}'")
            if transition['symbol'] not in alphabet:
                errors.append(f"Symbol '{transition['symbol']}' not in alphabet")

        # Verificar que cada estado tenga al menos una transición
        states_with_transitions = set(t['from_state'] for t in automaton_data['transitions'])
        for state in states:
            if state not in states_with_transitions and state != initial_state:
                errors.append(f"State '{state}' has no transitions and is not the initial state")

        return errors