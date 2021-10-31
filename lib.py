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

    def __init__(self,name, reminders = [] ):
        self.name = name
        for r in reminders:
            self.reminders.append(r)


def need(name, reminders = []):
    task = Task(name, reminders)
    return task

def at(reminders, task):
    reminders = []

    reminders 
    task = 
    return 
            )

def note(text, task):
    notes.append(
            Note(text)
            )

