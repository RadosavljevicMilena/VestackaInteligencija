"""Napisati funkciju koja određuje listu grana u grafu koje je neophodno obrisati da bi se ciklični graf 
transformisao u aciklični (da bi se u njemu eliminisali ciklusi)."""

from queue import LifoQueue

def edges_to_remove_cycles(graph):
    visited = set()
    edges_to_remove = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            #nemoj da gledas svog roditelja, gledaj samo svoju decu
            if neighbor == parent:
                continue
            #vec smo ga obisli, pravio bi se ciklus pa znamo da moze da se ukloni
            if neighbor in visited:
                edges_to_remove.add(tuple(sorted((node, neighbor))))
            else:
                dfs(neighbor, node)
    
    for node in graph:
        if node not in visited:
            dfs(node, None)
    
    return edges_to_remove

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['C','E', 'D']
}
print(edges_to_remove_cycles(graph)) 
