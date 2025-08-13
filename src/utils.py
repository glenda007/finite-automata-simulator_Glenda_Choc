import json

def load_automata_from_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data