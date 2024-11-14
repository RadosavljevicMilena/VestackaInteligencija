"""Napisati funkciju koja na osnovu zadatog težinskog neusmerenog grafa i zadatog (ciljnog) čvora G 
formira neusmereni težinski graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao 
dužina puta od čvora C do čvora G."""

from queue import Queue

from queue import Queue

def weighted_graph_with_heuristic(graph, g):
    # FIFO red za čuvanje čvorova i njihovih udaljenosti
    queue = Queue()
    queue.put((g, 0))  # Dodajemo ciljni čvor sa početnom udaljenostom 0
    distances = {node: float('inf') for node in graph}  # Postavljamo početne udaljenosti na beskonačnost
    distances[g] = 0  # Udaljenost od ciljnog čvora do njega samog je 0
    visited = set()  # Set za praćenje posećenih čvorova

    while not queue.empty():
        node, current_dist = queue.get()

        # Ako je čvor već posetio, preskoči ga
        if node in visited:
            continue
        visited.add(node)

        # Prolazimo kroz sve susede čvora i ažuriramo njihove udaljenosti
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_dist = current_dist + weight  # Ažuriramo udaljenost sa težinom potega
                if new_dist < distances[neighbor]:  # Ako je pronađena kraća udaljenost
                    distances[neighbor] = new_dist
                    queue.put((neighbor, new_dist))  # Dodajemo novog suseda u red

    # Na kraju vraćamo graf sa heuristikama (udaljenostima) i originalnim susedima
    result_graph = {}
    for node in graph:
        result_graph[node] = (distances[node], [(neighbor, weight) for neighbor, weight in graph[node]])

    return result_graph

# Testiranje sa težinskim grafom
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('D', 1), ('E', 3)],
    'C': [('A', 2), ('F', 1)],
    'D': [('B', 1)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 1), ('E', 1)]
}

print(weighted_graph_with_heuristic(graph, 'F'))
# Očekivani rezultat:
# {'A': (3, [('B', 1), ('C', 2)]),
#  'B': (4, [('A', 1), ('D', 1), ('E', 3)]),
#  'C': (1, [('A', 2), ('F', 1)]),
#  'D': (5, [('B', 1)]),
#  'E': (1, [('B', 3), ('F', 1)]),
#  'F': (0, [('C', 1), ('('E', 1)])}

