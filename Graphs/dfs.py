








from collections import deque


class Graph:
    root = dict()

    def addVertics(self, nodes):
        for node in nodes:
            if node not in self.root.keys():
                self.root[node] = []

    def addEdges(self, node, edges):
        if node in self.root.keys():
            for edge in edges:
                if edge in self.root.keys():
                    cur: list = self.root.get(node)
                    if edge not in cur:
                        cur.append(edge)


# WRTIE YOUR FUNCTION HERE


def track(nodes: list) -> dict:
    visited = dict()
    for node in nodes:
        visited[node] = False

    return visited


def dfs(list: dict, s: int) -> int:
    visited = track(list.keys())
    visited[s] = True
    stack = deque()
    stack.appendleft(s)
    while stack:
        cur = stack.pop()
        print(cur)
        for c in list.get(cur):
            if visited[c] == False:
                visited[c] = True
                stack.append(c)


def dfsRec(list: dict, s: int, visited: dict):
    visited[s] = True
    print(s)

    for key in list.keys():
        if visited[key] == False:
            dfsRec(list, key, visited)


# RECURSIVE SOLUTION
# ENDS HERE


g = Graph()

g.addVertics([0, 1, 2, 3, 4, 5, 6])
g.addEdges(0, [1, 2])
g.addEdges(1, [0, 3, 4])
g.addEdges(2, [0, 3])
g.addEdges(3, [2, 3])
g.addEdges(4, [1, 5])
g.addEdges(5, [4])
# g.addEdges(6, [4, 5])
# dfs(g.root, 0)
visited = track(g.root.keys())
dfsRec(g.root, 0, visited)
















