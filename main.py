from dataclasses import dataclass
from hashlib import sha1
import re
import json
import uuid
from typing import Callable, Match
from command import Command

from db import database, find_by_name
from history import history, update_history

hello_message = "-> "

# generate id
def generate_id(string):
    # return sha1(bytes(string, 'utf-8')).hexdigest()
    return str(uuid.uuid4())

def add_to_database(**kwargs):
    global database, history

    name = kwargs.get('name')
    text = kwargs.get('text')
    datetime = kwargs.get('datetime')
    entity_type = kwargs['entity_type'] # required
    parent = kwargs.get('parent')

    entity = {
        'type': entity_type,
        'name': name,
        'text': text,
        'datetime': datetime,
    }

    entity['id'] = generate_id(entity)
    database[entity['id']] = entity

    if not parent and len(history) > 0:
        parent = history[-1]

    if parent:
        par_type = entity['type']
        if par_type not in parent:
            parent[par_type] = []
        parent[par_type].append(entity['id'])
        entity['parent'] = parent['id']

    to_history = None
    if entity.get('type') == 'task':
        to_history = entity
        
    if not to_history and parent and parent.get('type') == 'task':
        to_history = parent
    
    if to_history:
        history.append(to_history)



"""
examples:
need "buy bread" - create task 'buy bread'
"""

def create(name, parent_name=None):
    task = find_by_name(parent_name)
    return {
        'name': name,
        'entity_type': 'task',
        'parent': task,
    }

def remind(datetime, parent_name=None):
    task = find_by_name(parent_name)
    return {
        'datetime': datetime,
        'entity_type': 'reminder',
        'parent': task,
    }
    
def note(text, parent_name=None):
    task = find_by_name(parent_name)
    return {
        'text': text,
        'entity_type': 'note',
        'parent': task
    }

def debug(*args):
    print('database:', json.dumps(database, indent=4, sort_keys=True))
    print('history:', json.dumps(history, indent=4, sort_keys=True))

def back(*args):
    if len(history) > 0:
        history.pop()



def traverse_task_tree(level, node, msg):
    tasks = node.get('task')
    if not tasks:
        return msg
        
    for task_id in tasks:
        task = database.get(task_id)
        tabs = "\t" * level
        msg = msg + f"\n{tabs} {task['name']}"
        children = task.get('task')
        if not children:
            continue
        if len(children) > 0:
            msg = traverse_task_tree(level+1, task, msg)
    return msg
def full_tree():
    return {
            'name': 'hill', 
            'task': [k for k, task in database.items() if not task.get('parent')],
            }

def tree(name=None):
    if name:
        if name == 'root':
            print('you are king of the hill')
            node = full_tree()
        else:
            node = find_by_name(name)
            if not node:
                print('i dont find task :(')
                return
    else:
        node = history[-1] if len(history) > 0 else None
    if not node:
        print('you are king of the hill')
        node = full_tree()
    msg = f"{node['name']}"
    msg = traverse_task_tree(1, node, msg)
    print(msg)

def root(*args):
    while len(history) != 0:
        history.pop()
    
commands = [
    Command(r"\s*need '(?P<name>[^']+)'$", create, 'create task or subtask for current task'),
    Command(r"\s*need '(?P<name>[^']+)' for '(?P<parent_name>[^']+)'$", create, 'create subtask'),
    Command(r"\s*remind in '(?P<datetime>[^']+)'$", remind, 'create reminder about current task'),
    Command(r"\s*note '(?P<text>[^']+)'$", note, 'add note for current task'),
    Command(r"\s*remind about '(?P<parent_name>[^']+)' in '(?P<datetime>[^']+)'$", remind, 'create reminder for task'),
    Command(r"\s*note about '(?P<parent_name>[^']+)' '(?P<text>[^']+)'$", note, 'create note for task'),
    Command(r"\s*back$", back, 'go to prev task in history'),
    Command(r"\s*debug$", debug, 'debug information'),
    Command(r"\s*tree$", tree, 'tree of subtasks of current task'),
    Command(r"\s*tree for '(?P<name>[^']+)'$", tree, 'tree of subtasks of specified task'),
    Command(r"\s*root$", root, 'go to begin of task tree'),
]

@dataclass
class Run:
    match: Match
    func: Callable


if __name__ == '__main__':
    while True:
        # global hello_message
        user_input = input(hello_message)
        splitted = re.split(r"and|,", user_input)
        have = []
        for s in splitted:
            for v in commands:
                match = re.match(v.pattern, s)
                if match:
                    have.append(
                        Run(match, v.func)
                    )
        
        for h in have:
            res = h.func(**h.match.groupdict())
            if res:
                add_to_database(**res)
            hello_message = update_history(hello_message)

        if len(have) == 0:
            help_message = "Usage: "
            for v in commands:
                help_message = help_message + "\t" + v.get_usage() + "\n"
            print(help_message)


