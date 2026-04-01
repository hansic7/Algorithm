import heapq
import copy

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
meta_graph = []

for _ in range(m):
    u, v, w = map(int, input().split())
    
    graph[u].append([v,w])
    graph[v].append([u,w])

    meta_graph.append((u,v,w,len(graph[u])-1,len(graph[v])-1))

def diikstra(graph, start_index):
    pq = []
    dist = [10e8] * (n+1)
    dist[start_index] = 0
    heapq.heappush(pq, (0, start_index))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            if dist[next_index] > prev_dist + w:
                dist[next_index] = prev_dist + w
                heapq.heappush(pq, (prev_dist + w, next_index))

    return dist


dist = diikstra(graph, 1)
dist_reverse = diikstra(graph, n)

result_before = dist[n]
result_after = 0

# for i in range(1, n):
#     tmp_graph = copy.deepcopy(graph)

#     for j in range(len(graph[i])):
#         v, w = graph[i][j]
#         if dist[i] + w == dist[v]:
#             tmp_graph[i][j][1] *= 2
#             break

#     tmp_dist = diikstra(tmp_graph)
    
#     result_after = max(result_after, tmp_dist[n])


for u, v, w, u_index, v_index in meta_graph:
    if dist[u] + w + dist_reverse[v] == result_before \
    or dist[v] + w + dist_reverse[u] == result_before:
        tmp_graph = copy.deepcopy(graph)
        tmp_graph[u][u_index][1] *= 2
        # tmp_graph[v][v_index][1] *= 2
        tmp_dist = diikstra(tmp_graph, 1)
        result_after = max(result_after, tmp_dist[n])

print(result_after - result_before)


# Please write your code here.
