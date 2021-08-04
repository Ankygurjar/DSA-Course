





from collections import deque


class Graph:
    root = dict()

    def nodes(self, nodes: list):
        for node in nodes:
            if node not in self.root.keys():
                self.root[node] = []

    def vertices(self, node, edges: list):
        if node in self.root.keys():
            cur: list = self.root.get(node)
            for edge in edges:
                if edge not in cur:
                    cur.append(edge)


# WRITE CODE HERE


def shortestPath(graph: dict, s: int):
    visited, dist = {}, {}
    for key in graph.keys():
        visited[key] = False
        dist[key] = float("inf")
    visited[s] = True
    dist[s] = 0
    queue = []
    queue.append(s)
    while queue:
        cur = queue.pop(len(queue) - 1)
        for c in graph.get(cur):
            if visited[c] == False:
                visited[c] = True
                dist[c] = dist[cur] + 1
                queue.append(c)

    print(dist)


# ENDS HERE

g = Graph()

g.nodes([0, 1, 2, 3])
g.vertices(0, [1, 2])
g.vertices(1, [2, 3])
g.vertices(2, [1, 3, 0])
g.vertices(3, [1, 2])
myList: list = g.root.values()
shortestPath(g.root, 3)


















