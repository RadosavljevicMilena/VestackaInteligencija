"""Napisati funkciju koja na osnovu zadatog usmerenog grafa i zadatog čvora S određuje čvor 
(čvorove) koji su najudaljeniji od njega. Udaljenost se određuje kao dužina najkraćeg puta između 
dva čvora. Dužina puta se određuje kao broj potega koji čine taj put."""

from queue import Queue

def farthest_nodes_from_s(graph, s):
    queue = Queue()
    queue.put((s, 0))
    visited = {s}
    max_dist = 0
    farthest_nodes = []

    while not queue.empty():
        node, dist = queue.get()
        if dist > max_dist:
            max_dist = dist
            #U prvom trenutku kada naidjemo na najudaljeniji i kasnije ga prepisujemo svaki put kada nadjemo udaljeniji
            farthest_nodes = [node]
        elif dist == max_dist:
            #samo ga dodajemo u listu sa tom udaljenoscu
            farthest_nodes.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, dist + 1))

    return farthest_nodes

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(farthest_nodes_from_s(graph, 'A'))
# Očekivani rezultat: ['D', 'E', 'F']
