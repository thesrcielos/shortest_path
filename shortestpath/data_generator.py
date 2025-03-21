import random
from shortestpath import constants
from collections import deque

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

    bfs_path(answer, start, goal, limit)
    return [answer, start, goal, m]

def bfs_path(adj_list, start, end, limit):
    queue = deque([(start, [start])])  # (current node, path)
    visited = set()
    closest_path = None
    
    while queue:
        node, path = queue.popleft()
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == end:
            return # Se encontró el destino
        
        for neighbor,_ in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                
                if closest_path is None or len(path) + 1 < len(closest_path):
                    closest_path = path + [neighbor]
    
    last_node = start
    if closest_path is not None:
        last_node = closest_path[-1]
    adj_list[last_node].append([end, random.randint(0, limit)])


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)
