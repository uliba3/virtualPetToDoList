import json
import os

def load_data():
    if not os.path.exists('todo.json'):
        with open('todo.json', 'w') as file:
            json.dump([], file)
        return []
    else:
        with open('todo.json', 'r') as file:
            data = json.load(file)
        return data

def save_data(data):
    with open('todo.json', 'w') as file:
        json.dump(data, file)

def add_event(data, event):
    data = load_data()
    data.append(event)
    save_data(data)

def remove_event(data, index):
    data = load_data()
    del data[index]
    save_data(data)

def edit_event(data, index, event):
    data = load_data()
    data[index] = event
    save_data(data)