import os

path = "tests.txt"

async def add_test(keys):
    last_id = 1
    if os.path.exists(path):
        with open(path, "r") as file:
            ls = file.readlines()
            for line in ls:
                last_id = max(last_id, int(line.split()[0]))


    with open(path, 'a') as file:
        file.write(f"{last_id + 1} {keys}")

    return last_id + 1

async def show_all_test():
    tests = "Teslar ro'yxati : \n"
    if os.path.exists(path):
        with open(path, "r") as file:
            ls = file.readlines()
            for line in ls:
                tests += f"{line}\n"

    return tests
