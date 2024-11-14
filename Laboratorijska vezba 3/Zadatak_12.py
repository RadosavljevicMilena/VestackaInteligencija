"""Napisati funkciju koja pronalazi puteve zadate dužine u neusmerenom grafu između dva zadata 
čvora."""

from queue import LifoQueue

def paths_of_length(graph, start, end, length):
    def dfs(node, path_length, visited):
        if path_length == length:
            return 1 if node == end else 0
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                count += dfs(neighbor, path_length + 1, visited)
                visited.remove(neighbor)
        return count

    return dfs(start, 0, {start})

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(paths_of_length(graph, 'A', 'E', 3))  # Očekivani rezultat: 1
