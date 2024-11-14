"""Napisati funkciju koja pronalazi put u neusmerenom grafu između dva zadata čvora, pri čemu put 
prolazi kroz treći zadati čvor."""

from queue import Queue

def bfs(graph, start, goal):
    """Generalizovana funkcija za BFS koja traži put od start do goal."""
    queue = Queue()
    queue.put((start, [start]))
    visited = {start}
    
    while not queue.empty():
        node, path = queue.get()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, path + [neighbor]))
    
    return None  # Ako nije pronađen put

def path_via_node(graph, start, middle, end):
    # Pronađi put od start do middle
    path_to_middle = bfs(graph, start, middle)
    if path_to_middle is None:
        return None
    
    # Pronađi put od middle do end
    path_from_middle = bfs(graph, middle, end)
    if path_from_middle is None:
        return None

    # KombinujE put do middle (bez middle na kraju) i put od middle do end
    return path_to_middle[:-1] + path_from_middle

# Testiranje sa grafom
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(path_via_node(graph, 'A', 'B', 'F'))
# Očekivani rezultat: ['A', 'B', 'E', 'F']
