
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    print(node, end=' ')
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')

print("Graph:")
g.display()

print("\nBFS from A:")
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(g.graph, 'A')

print("\n\nDFS (Iterative) from A:")
dfs_iterative(g.graph, 'A')

print("\n\nDFS (Recursive) from A:")
dfs_recursive(g.graph, 'A')
