"""Napisati funkciju koja određuje visinu stabla traženja (broj nivoa u stablu traženja), za algoritam 
obilaska grafa po širini, koje se formira za zadati polazni čvor i zadati graf.  """

from queue import Queue

def bfs_tree_height(graph, start):
    q_node = Queue()
    q_node.put((start, 0))
    visited = {start}
    max_level = 0

    while not q_node.empty():
        node, level = q_node.get()
        max_level = max(max_level, level)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q_node.put((neighbor, level + 1))
    
    return max_level

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs_tree_height(graph, 'A'))  # Očekivani rezultat: 2
