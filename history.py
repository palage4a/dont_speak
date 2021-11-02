history = []


def update_history(msg):
    if len(history) == 0:
        return "-> "

    current = history[-1]
    return f"{current['type']} '{current['name']}' -> "

