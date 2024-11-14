"""Napisati funkciju koja određuje broj čvorova do kojih može da se dođe od zadatog čvora, tako da 
je dužina puta do čvora jednaka zadatoj vrednosti. Obići samo neophodne čvorove. """

from queue import Queue

def nodes_at_distance(graph, start, target_distance):
    queue = Queue()
    queue.put((start, 0))
    visited = {start}
    count = 0
    
    while not queue.empty():
        node, dist = queue.get()
        if dist == target_distance:
            count += 1
        elif dist < target_distance:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.put((neighbor, dist + 1))
    
    return count

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(nodes_at_distance(graph, 'A', 2))  # Očekivani rezultat: 3 (čvorovi D, E, F)
