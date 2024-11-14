""" Napisati funkciju koja određuje da li je usmereni graf jako povezan graf (da li postoji put između 
bilo koja dva čvora u grafu)."""

from queue import LifoQueue

def is_strongly_connected(graph):
    def dfs(start):
        stack = LifoQueue()
        stack.put(start)
        visited = {start}
        
        while not stack.empty():
            node = stack.get()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.put(neighbor)
        return visited

    all_nodes = set(graph.keys())
    for node in graph:
        if dfs(node) != all_nodes:
            return False
    
    return True

graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': []
}
print(is_strongly_connected(graph))  # Očekivani rezultat: False
