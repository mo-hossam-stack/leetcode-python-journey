def bfs(graph, root):
    visited = [root]
    queue = [root]

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

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

print(bfs(graph, 'S'))  # Output: ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'J', 'G', 'I', 'H']