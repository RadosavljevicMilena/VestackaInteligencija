"""Napisati funkciju koja formira stablo traženja za zadati graf, zadati polazni čvor i izabrani algoritam 
koji se koristiti za obilazak stabla. Student sam bira algoritam za koji se formira stablo traženja."""

from queue import Queue, LifoQueue

def search_tree(graph, start, algorithm="bfs"):
    tree = {start: []}
    visited = {start}
    container = Queue() if algorithm == "bfs" else LifoQueue()
    container.put((start, None))
    
    while not container.empty():
        node, parent = container.get()
        if parent is not None:
            tree[parent].append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                container.put((neighbor, node))
                tree[node] = tree.get(node, [])
    
    return tree

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}
print(search_tree(graph, 'A', 'bfs'))
# Očekivani rezultat za BFS: {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'E': ['F']}
