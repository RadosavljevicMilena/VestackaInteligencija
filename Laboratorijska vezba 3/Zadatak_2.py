"""Napisati funkciju koja određuje broj disjunktnih puteva između dva zadata čvora u grafu. Rešenje 
ne mora biti optimalno prema broju puteva. Dozvoljeno je više puta pozvati algoritam obilaska 
grafa."""

from queue import LifoQueue

def disjoint_paths_count(graph, start, end):
    def dfs(node, visited):
        if node == end:
            return 1
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                count += dfs(neighbor, visited)
                visited.remove(neighbor)
        return count
    
    return dfs(start, {start})

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(disjoint_paths_count(graph, 'A', 'F'))  # Očekivani rezultat: 2
