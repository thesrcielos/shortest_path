import logging, math, heapq
from shortestpath import constants

def bellman_ford(adjList, start, goal):
    size = len(adjList)
    distances = [math.inf] * size
    distances[start] = 0
    prev = [None] * size
    
    for _ in range(len(adjList) - 1):
        for i in range(len(adjList)):
            for neighbor, weight in adjList[i]:
                distance = distances[i] + weight
                if distances[neighbor] > distance:
                    distances[neighbor] = distance
                    prev[neighbor] = i

    for i in range(len(adjList)):
            for neighbor, weight in adjList[i]:
                distance = distances[i] + weight
                if distances[neighbor] > distance:
                    return None

    return rebuild_path(prev, start, goal)

def dijkstra(adjList, start, goal):
    pq = [(0,start)]
    size = len(adjList)
    distances = [math.inf] * size
    distances[start] = 0
    prev = [None] * size

    while pq:
        weight_vertice, vertice = heapq.heappop(pq)
        if weight_vertice > distances[vertice]:
            continue

        if vertice == goal:
            return rebuild_path(prev, start, goal)
        
        for neighbor, weight in adjList[vertice]:
            distance = weight_vertice + weight
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                prev[neighbor] = vertice
    
    return []

def heuristic(a, b):
    return abs(a - b)

def a_star(adjList, start, goal):
    pq = [(0,start)]
    size = len(adjList)
    distances = {start: 0} 
    prev = [None] * size

    while pq:
        _, vertice = heapq.heappop(pq)
        weight_vertice = distances[vertice]
        if vertice == goal:
            return rebuild_path(prev, start, goal)

        for neighbor, weight in adjList[vertice]:
            distance = weight_vertice + weight
            if neighbor not in distances or distances[neighbor] > distance:
                distances[neighbor] = distance
                priority = distance + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                prev[neighbor] = vertice

    return []

def rebuild_path(paths, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = paths[current]
            if current == None:
                return []
        path.append(start)
        return path[::-1]


