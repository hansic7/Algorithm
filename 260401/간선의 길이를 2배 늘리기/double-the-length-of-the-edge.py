import heapq
import copy

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
meta_graph = []

for _ in range(m):
    u, v, w = map(int, input().split())
    
    graph[u].append([v,w])
    graph[v].append([u,w])

    meta_graph.append((u,v,len(graph[u])-1,len(graph[v])-1))

def diikstra(graph):
    pq = []
    dist = [10e8] * (n+1)
    dist[1] = 0
    heapq.heappush(pq, (0, 1))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            if dist[next_index] > prev_dist + w:
                dist[next_index] = prev_dist + w
                heapq.heappush(pq, (prev_dist + w, next_index))

    return dist


dist = diikstra(graph)
result_before = dist[n]

result_after = 0


for i in range(1, n):
    tmp_graph = copy.deepcopy(graph)

    for j in range(len(graph[i])):
        v, w = graph[i][j]
        if dist[i] + w == dist[v]:
            tmp_graph[i][j][1] *= 2
                    
    tmp_dist = diikstra(tmp_graph)
    
    result_after = max(result_after, tmp_dist[n])

print(result_after - result_before)


# Please write your code here.
