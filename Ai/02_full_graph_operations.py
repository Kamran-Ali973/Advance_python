
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def remove_vertex(self, v):
        if v in self.graph:
            self.graph.pop(v)
        for node in self.graph:
            if v in self.graph[node]:
                self.graph[node].remove(v)

    def remove_edge(self, u, v, directed=False):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if not directed and v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def has_edge(self, u, v):
        return u in self.graph and v in self.graph[u]

    def neighbors(self, v):
        return self.graph.get(v, [])

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
