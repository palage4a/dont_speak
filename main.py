from hashlib import sha1
import re

from db import database
from history import history

hello_message ="-> "

# generate id
def hash(string):
    return sha1(bytes(string, 'utf-8')).hexdigest()

# def add_to_database(name, type_, parent=None):
def add_to_database(**kwargs):
    global database, history
    name = kwargs['name']
    entity_type = kwargs['type']
    parent = kwargs['parent']
    entity_id = hash(name)

    entity = {
        'id': entity_id,
        'type': entity_type,
        'name': name,
    }

    database[entity_id] = entity

    if not parent and len(history) > 0:
        parent = history[-1]

    if parent:
        par_type = entity['type']
        if par_type not in parent:
            parent[par_type] = []
        parent[par_type].append(entity['id'])

    history.append(entity)


def update_hmsg():
    global hello_message
    if len(history) > 0:
        current = history[-1]
        hello_message = f"{current['type']} \"{current['name']}\" -> "
    else:
        hello_message = "-> "


while True:
    user_input = input(hello_message)
    match = re.split(r"\W+", user_input)

    from proc_tree import tree
    if match:
        res = tree.process(0, match)
        if not res:
            continue
        add_to_database(**res)
        update_hmsg()
