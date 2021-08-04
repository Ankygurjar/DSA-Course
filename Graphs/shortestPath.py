from collections import deque

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


shortestPath(g.root, 3)


















