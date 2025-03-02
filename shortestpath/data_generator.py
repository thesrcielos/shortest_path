import random
from shortestpath import constants


def get_random_graph(size, limit=constants.MAX_VALUE):
    if size == 0:
        return []
    answer = [[]] * size
    m = 0
    for i in range(size):
        numRelations = random.randint(0, size // 10)
        relations = set()
        for _ in range(numRelations):
            vert = random.randint(0, size - 1)
            if vert == i:
                continue
            relations.add(vert)
        for elem in relations:
            m+=1
            answer[i].append([elem, random.randint(0, limit)])

    start = random.randint(0, size - 1)
    goal = random.randint(0, size - 1)

    while start == goal and size > 1:
        goal = random.randint(0, size - 1)

    return [answer, start, goal, m]

def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)
