def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(reversed(graph[current]))

    return visited
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['E'],
    'C': ['F', 'J'],
    'D': ['G'],
    'E': ['I', 'J'],
    'F': [],
    'G': ['H'],
    'H': [],
    'I': [],
    'J': []
}

print(dfs(graph, 'S'))