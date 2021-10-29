class Task:
    name = ''
    description = '' # optional
    datetime = ''
    gentime = ''

    reminders = []
    notes = []

class Note:
    name = '' # optional
    text = ''
    datetime = ''
    gentime = ''

    reminders = []

class Reminder:
    tag = ''
