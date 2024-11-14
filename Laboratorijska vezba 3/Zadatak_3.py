"""Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadatog (početnog) čvora S formira 
niz čvorova sa njihovim udaljenostima od čvora S. Udaljenost se određuje kao dužina najkraćeg 
puta od čvora A do nekog čvora. Dužina puta se određuje kao broj potega koji čine taj put."""

from queue import Queue

def distances_from_node(graph, start):
    q = Queue()
    q.put((start, 0))
    visited = {start}
    distances = {}
    
    while not q.empty():
        node, dist = q.get()
        distances[node] = dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put((neighbor, dist + 1))
    
    return distances

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(distances_from_node(graph, 'A'))
# Očekivani rezultat: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}

