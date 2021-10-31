import re
import json
import functools

from db import database, find_in_database
from utils import hash
from history import history

# from lib import *

# var 1
# json.dumps(
#     need("buy butter").at("16:30").done(), indent=4,
#         )

# json.dumps(
#     at("16:30").need("buy butter").done(), indent=4
#         )

# var 2
# need("buy butter", at(["16:30", "15:20"]))

# at("16:30", need("buy butter"))

# task = { 'name': '' }
# note = { 'text': '' }
# reminder = {'time': ''}

cur_task = None

# need "<name>" at "<time>"
while True:
    if cur_task:
        if len(cur_task.reminders) == 0:
            remind_time = input("want me to remind at ...?\n")
            reminder = {
                    'time': remind_time,
                    }
            cur_task.reminders.append(reminder)
        if len(cur_task.notes) == 0:
            note_text = input('any description about task?\n')
            note = {
                    'text': note_text,
                    }
            cur_task.notes.append(note)

    command = input("what do you need?\n")
    # split = re.split(r"\W+", command)


    time = re.search(r"[0-9]{1,2}:[0-9]{1,2}", command)


    if split[0] == 'debug':
        print('database:', json.dumps(database, indent=4, sort_keys=True))
        print('history:', json.dumps(history, indent=4, sort_keys=True))

    if split[0] == 'need':
        _id = hash(task['name'])
        task = {
                'id': _id,
                'name': split[1],
                'reminders': [],
                'notes': [],
                }

        database[_id]  = task
        cur_task = task

        if split[2] == 'at':
            reminder = {
                    "text": '',
                    'time': split[2]
                    }
            task.reminders.append(reminder)

    if split[0] == 'remind':
        reminder = {}
        if split[1] == 'at':
            reminder['time'] = split[2]

        if split[1] == 'about':
            inters = find_in_database(split[2])
            print(inters)



