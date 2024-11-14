"""Napisati funkciju koja određuje put između zadatog polaznog i ciljnog čvora neusmerenog grafa 
tako što istovremeno pokreće traženje po širini od polaznog i od ciljnog čvora. Traženje se završava 
kada se nađe prvi zajednički čvor za oba traženja."""

from queue import Queue

def bidirectional_bfs(graph, start, end):
    if start == end:
        return [start]

    queue_start, queue_end = Queue(), Queue()
    #ovaj niz je put zapravo
    queue_start.put((start, [start]))
    queue_end.put((end, [end]))
    visited_start, visited_end = {start: [start]}, {end: [end]}
    
    def expand(queue, visited, other_visited):
        node, path = queue.get()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = path + [neighbor]
                queue.put((neighbor, visited[neighbor]))
            if neighbor in other_visited:
                return neighbor
        return None

    while not queue_start.empty() and not queue_end.empty():
        intersect = expand(queue_start, visited_start, visited_end)
        if intersect:
            #:-1 uzimamo od pocetka bez zadnjeg
            return visited_start[intersect][:-1] + list(reversed(visited_end[intersect]))
    
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bidirectional_bfs(graph, 'A', 'E'))
# Očekivani rezultat: ['A', 'C', 'F'] ili ['A', 'B', 'E', 'F']
