""" Breadth-First Search (BFS) """

def bfs(graph, start):
    """
    Breadth-first search (BFS) alghorhythm
    """
    visited = set()
    queue = [start]
    order = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return order
