from flask import Flask, jsonify, request 
from automaton import Automaton
from validator import AutomatonValidator
from diagram_generator import DiagramGenerator
from string_processing import StringProcessing
import json
import os 

# crea un directorio para los diagramas generados 
app = Flask(__name__)
os.makedirs('generate_diagrams', exist_ok=True) # crea el directorio si no existe

# endpoint para procesar autómatas
@app.route('/process_automata', methods=['POST'])
# Funcion para procesar los automatas
def process_automata():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        autoamta_data = json.load(file)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 400
    
    if not isinstance(autoamta_data, list):
        return jsonify({"error": "Expected a list of automata"}), 400

    results = []

    # Validar y procesar cada autómata
    for automaton_data in autoamta_data:
        result = {"id": automaton_data.get('id'), "success": False}

        validation_errors = AutomatonValidator.validate(automaton_data)
        if validation_errors:
            result["error_description"] = "; ".join(validation_errors)
            results.append(result)
            continue

        # Crear una instancia del autómata
        automaton = Automaton(
            id=automaton_data['id'],
            name=automaton_data['name'],
            initial_state=automaton_data['initial_state'],
            acceptance_states=automaton_data['acceptance_states'],
            alphabet=automaton_data['alphabet'],
            states=automaton_data['states'],
            transitions=automaton_data['transitions'],
        )

        # Generar el diagrama 
        try:
            diagram_path = DiagramGenerator.generate_diagram(automaton)
            result["diagram_path"] = diagram_path
        except Exception as e:
            result["error_description"] = f" Diagram generation failed : {str(e)}"
            results.append(result)
            continue

        test_strings = automaton_data.get('test_strings', [])
        input_results = []

        # Procesar cada cadena de prueba
        for test_string in test_strings:
            is_accepted = StringProcessing.process_string(automaton, test_string)
            input_results.append({"input": test_string, "accepted": is_accepted})

        # Almacenar los resultados de la validación
        result["success"] = True
        result["inputs_validation"] = input_results
        results.append(result)

    # Devolver los resultados
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)