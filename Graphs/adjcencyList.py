








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


g = Graph()

g.nodes([1, 0, 2, 3])
g.vertices(0, [1, 2])
g.vertices(1, [0, 2])
g.vertices(2, [0, 1, 3])
g.vertices(3, [2])
myList: list = g.root.values()
print(myList)
# print(g.root)















