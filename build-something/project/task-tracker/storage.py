import json

FILE_NAME = "tasks.json"

def get_default_structure():
    return { 
        "last_id": 0,
        "tasks": [] 
    }

def load_state():
    default_structure = get_default_structure()
    try:
        with open(FILE_NAME, "r") as file:
            data =  json.load(file)

            # Validate the loaded data structure   
            # isinstance is used to check if the data is a dictionary and if it has a "tasks" key with a list value
            if isinstance(data, dict) and "tasks" in data and isinstance(data["tasks"], list):
                return data

            return default_structure

    except FileNotFoundError:
        return default_structure
    except json.JSONDecodeError:
        return default_structure

def save_state(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
