# Depth First Traversal for a Graph

from collections import defaultdict
class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
  def add_edge(self, u, v):
    self.graph[u].append(v)
  def dfs(self, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.add(vertex)
        print(vertex)
        for neighbor in self.graph[vertex]:
          stack.append(neighbor)
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.dfs(0)