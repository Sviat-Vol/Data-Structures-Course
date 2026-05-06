""" Depth-First Search (DFS) """

def dfs(graph, start, visited=None, visited_l=None):
    """
    Depth-аirst іearch (DFS) alghorhythm
    """
    if visited is None:
        visited = set()
    if visited_l is None:
        visited_l = []
    visited.add(start)
    visited_l.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, visited_l)
    return visited_l
