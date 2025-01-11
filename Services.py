import os

path = "tests.txt"

def add_test(keys):
    last_id = 1
    if os.path.exists(path):
        with open(path, "r") as file:
            ls = file.read().split()
            last_id = max(last_id, int(ls[0]))

    with open(path, 'a') as file:
        file.write(f"{last_id + 1} {keys}")

    return last_id + 1
