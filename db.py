import re

database = {}

# TODO: explain what is and use it
def find_in_database(pattern):
    words = re.split(r'\W+', pattern)
    intersections = {}
    for task in database.items():
        for word in words:
            if word in task['name']:
                if task['id'] in intersections.keys():
                    intersections[task['id']] = intersections[task['id']] + 1
                else:
                    intersections[task['id']] = 1
    return intersections



def find_by_name(name):
    if not name:
        return None

    for task in database.values():
        if name in task['name']:
            return task