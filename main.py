from hashlib import sha1
import json
import uuid
import re

entity_types = (
    'task',
    'reminder',
    'note',
)


create_cmds = (
        'add',
        'create'
        )

database = {
}

last_cmd = None

history = []

hello_message ="-> "


# generate id
def hash(string):
    return sha1(bytes(string, 'utf-8')).hexdigest()

def add_to_database(name, type_, parent=None):
    global database, history
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

    if match:
        if match[0] == 'debug':
            print('database:')
            print(json.dumps(database, indent=4, sort_keys=True))
            print('history:')
            print(json.dumps(history, indent=4, sort_keys=True))

        if match[0] == 'up':
            if len(history) == 0:
                print('already in air')
            else:
                history.pop()

        if match[0] in create_cmds:
            entity_type = match[1]
            if entity_type not in entity_types:
                print(f'warn: {entity_type} not allowed entity type')
                continue

            parent = None
            if len(match) == 5 and match[3] in ['in', 'to']:
                try:
                    parent_id = hash(match[4])
                    parent = database[parent_id]
                except Exception as e:
                    print('find parent err: ', err)

            add_to_database(match[2], match[1], parent)

        update_hmsg()
