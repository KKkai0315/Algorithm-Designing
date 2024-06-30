def shortest_path(N, M, S, edges):
    dist = [float('inf')] * N
    dist[S] = 0
    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for d in dist:
        print(d)
N, M, S = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
shortest_path(N, M, S, edges)
