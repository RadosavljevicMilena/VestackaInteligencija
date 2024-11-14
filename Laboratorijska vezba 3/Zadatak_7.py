"""Napisati funkciju koja na osnovu zadatog neusmerenog grafa i dva zadata (ciljna) čvora G1 i G2 
formira neusmereni graf sa heuristikom. Heuristika proizvoljnog čvora C se određuje kao 
udaljenost čvora C do bližeg od čvorova G1 i G2. Udaljenost se određuje kao dužina najkraćeg puta 
između dva čvora. Dužina puta se određuje kao broj potega koji čine taj put. Dozvoljeno je najviše 
dva puta pozvati prilagođeni algoritam obilaska grafa. """

#Ovde nam je svejedno da li je LifoQueue ili Queue

from queue import Queue

def heuristic_graph_dual(graph, g1, g2):
    def bfs_distance(start):
        queue = Queue()
        queue.put((start, 0))
        visited = {start}
        distances = {}
        
        while not queue.empty():
            node, dist = queue.get()
            distances[node] = dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.put((neighbor, dist + 1))
        
        return distances

    distances_g1 = bfs_distance(g1)
    distances_g2 = bfs_distance(g2)
    return {node: (min(distances_g1.get(node), distances_g2.get(node)), graph[node]) for node in graph}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(heuristic_graph_dual(graph, 'D', 'F'))
#Ocekivani rezultat: {'A': (2, ['B', 'C']), 'B': (1, ['A', 'D', 'E']), 'C': (1, ['A', 'F']), 'D': (0, ['B']), 'E': (1, ['B', 'F']), 'F': (0, ['C', 'E'])}