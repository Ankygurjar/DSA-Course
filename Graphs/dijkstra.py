# CODE HERE


def findMinVertex(weight: list, visited: dict) -> int:
    minVertex = -1
    for i in range(len(weight)):
        if visited[i] == False and (minVertex == -1 or weight[i] < weight[minVertex]):
            minVertex = i

    return minVertex


def dijkstra(adjMatrix):
    v = len(adjMatrix)
    visited = [False] * v
    distance = [float("inf")] * v
    distance[0] = 0

    for i in range(v - 1):
        minVertex = findMinVertex(distance, visited)
        visited[minVertex] = True
        for j in range(0, v):
            if (
                adjMatrix[minVertex][j] != 0
                and visited[j] == False
                and distance[minVertex] != float("inf")
            ):
                newDistance = distance[minVertex] + adjMatrix[minVertex][j]
                if newDistance < distance[j]:
                    distance[j] = newDistance

    print(distance)


# CODE ENDS

# v = int(input("Enter the number of nodes"))

# adjMatrix = [[0 for i in range(v)] for j in range(v)]

# for i in range(len(adjMatrix)):
#     adjMatrix[i] = list(map(int, input().split()))
adjMatrix = [[0, 5, 3], [5, 0, 1], [3, 1, 0]]
dijkstra(adjMatrix)
