from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 使用默认字典存储图
        self.V = vertices  # 图的节点数量
        self.capacity = {}  # 容量字典

    # 添加有向边
    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)  # 添加反向边，初始容量为0
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0  # 反向边初始容量为0

    # 使用BFS寻找增广路径
    def bfs(self, source, sink, parent):
        visited = [False] * (self.V + 1)
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in self.graph[u]:
                if visited[v] == False and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == sink:
                        return True
        return False

    # Ford-Fulkerson算法实现
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.V + 1)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

        return max_flow


data = input().split()

N = int(data[0])
M = int(data[1])
S = int(data[2])
T = int(data[3])

graph = Graph(N)

for _ in range(M):
    data = input().split()
    u = int(data[0])
    v = int(data[1])
    w = int(data[2])
    graph.add_edge(u, v, w)

print(graph.ford_fulkerson(S, T))
