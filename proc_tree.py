import json

from db import database
from history import history

entity_types = (
    'task',
    'reminder',
    'note',
)

class Node:
    out = {
        'name': '',
        'type': '',
        'parent':''
    }

    def __init__(self, key, func):
        self.key = ''
        self.func = func
        self.children = {}

    def insert(self, key, node):
        self.children[key] = node
        return self.children[key]

    def get(self, key):
        return self.children[key]

    def process(self, index, match):
        index = 0
        cmd = match[index]
        if cmd not in self.children.keys():
            print(f"warn: {cmd} isn't allowed command")
        return self.children[cmd].func(self.children[cmd], 0, match)



def debug(node, _, match):
    if not match[0] == 'debug':
        return
    print('database:', json.dumps(database, indent=4, sort_keys=True))
    print('history:', json.dumps(history, indent=4, sort_keys=True))

def up(node, index,  match):
    if index != 0:
        return
    if len(node.history) == 0:
        print('already in air')
    else:
        node.history.pop()

# create <type> <name> [to <name>]
def create(self, index, match):
    entity_type = match[index+1]
    if entity_type not in entity_types:
        print(f'warn: {entity_type} not allowed entity type')
        return None

    self.out['name'] = match[2]
    self.out['type'] = match[1]

    parent = None

    """
    print(self.children)
    for k, v in self.children.items():
        print(k, v)
    """
    try:
        if len(match) > 3 and match[3] in ['to']:
            self.out = self.children['to'].func(self.children['to'], 3, match)
    except Exception as e:
        print("to find err: ", e)

    return self.out

def to_(self, index, match):
    try:
        parent_id = hash(match[index+1])
        parent = database[parent_id]
    except Exception as e:
        print('find parent err: ', e)

def and_(self, index, match):
    return

tree = Node({}, None)

debug_node = Node('debug', debug)
tree.insert('debug', debug_node)

create_node = Node('add', create)
create_node = tree.insert('add', create_node)
# create_node.insert('with', Node('with', with_))
create_node.insert('to', Node('to', to_))

and_node = create_node.insert('and', Node('and', and_))
and_node.insert('create', create_node)
