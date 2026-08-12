# Breadth First Search
from collections import deque

def bfs(graph,start):
    visited = set()

    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)



graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs(graph, "A")


#implementing stack using list
# we can also implement stack using dequeue

def dfs(graph , start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour) 



graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

dfs(graph, "A")