



def track(nodes):
      track = {}
      for node in nodes:
          track[node] = False

      return track


def bfsOfGraph(V, adj):
      # code here
      for i in range(V):
          addGraph(i, adj[i])
      track = track(self.root.keys())
      nodes = []
      queue = []
      queue.append(next(iter(self.root)))
      nodes.append(queue[0])
      track[queue[0]] = True
      while queue:
          cur = queue.pop(0)
          neighbours = self.root.get(cur)
          for n in neighbours:
              if track[n] == False:
                  track[n] = True
                  nodes.append(n)
                  queue.append(n)
      return nodes


















