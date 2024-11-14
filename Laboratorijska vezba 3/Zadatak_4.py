""" Napisati funkciju koja na osnovu zadatog neusmerenog grafa i zadatog (ciljnog) čvora G formira 
neusmereni graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao udaljenost čvora 
C od čvora G. Udaljenost se određuje kao dužina najkraćeg puta između dva čvora. Dužina puta se 
određuje kao broj potega koji čine taj put."""

from queue import Queue

def heuristic_graph(graph, g):
    queue = Queue()
    queue.put((g, 0))
    visited = {g}
    distances = {}

    while not queue.empty():
        node, dist = queue.get()
        distances[node] = dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, dist + 1))

    heuristic_graph = {node: (distances[node], graph[node]) for node in graph}
    return heuristic_graph

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(heuristic_graph(graph, 'F'))
# Očekivani rezultat: {'A': (2, ['B', 'C']), 'B': (2, ['A', 'D', 'E']), 'C': (1, ['A', 'F']), 'D': (3, ['B']), 'E': (1, ['B', 'F']), 'F': (0, ['C', 'E'])}
