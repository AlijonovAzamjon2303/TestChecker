import os

path = "tests.txt"
path_act = "answers.txt"

async def add_test(keys):
    last_id = 1
    if os.path.exists(path):
        with open(path, "r") as file:
            ls = file.readlines()
            for line in ls:
                last_id = max(last_id, int(line.split()[0]))


    with open(path, 'a') as file:
        file.write(f"{last_id + 1} {keys}\n")

    return last_id + 1

async def show_all_test():
    tests = ""
    if os.path.exists(path):
        with open(path, "r") as file:
            tests = file.read()

    return tests

async def clear():
    if os.path.exists(path):
        os.remove(path)
    else:
        return 0

async def add_ans(chat_id, test_id, first_name, answer):
    tests = []
    with open(path, "r") as file:
        tests = file.readlines()

    answer = answer.split()

    cnt = 0
    for test in tests:
        test = test.split()
        if test[0] == answer[0]:
           for i in range(min(len(test[1]), answer[1])):
               if test[1][i] == answer[1][i]:
                   cnt += 1

    with open(path_act, "a") as file:
        file.write(f"{chat_id} {test_id} {first_name} {answer} {cnt}")

    return cnt

async def show_all_act():
    acts = ""
    with open(path_act, "r") as file:
        for line in file.readlines():
            line = line.strip()
            acts += line + "\n"

    return acts