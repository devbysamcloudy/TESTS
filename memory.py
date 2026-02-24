import json
import os

MEMORY_FILE = "memory.json"
user_name = None

if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
            user_name = data.get('name')
    except:
        pass


def set_name (name):
    global user_name
    user_name = name
    return f"I'll call you {name}"

def get_name():
    return user_name if user_name else  "unknown"
def greet():
    if user_name:
        return  f"Hello {user_name}"

    else:
        return "Hello. What's your name?"
