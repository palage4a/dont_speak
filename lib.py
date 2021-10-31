class Reminder:
    def __init__(self, time, task):
        self.time = time
        self.task = task


class Note:
    def __init__(self, text, task):
        self.text = text
        self.task = task

class Task:
    reminders = []
    notes = []
    subtasks = []

    def __init__(self, name, reminders = [] ):
        self.name = name
        for r in reminders:
            self.reminders.append(r)


"""
1 - name
2 - reminder
3 - note
"""
# def need(*args):
#     while True:
#         if len(args) == 0:
#             name = input("how about name?")
#             if name:


# def at(reminders, task):
# def note(text, task):

