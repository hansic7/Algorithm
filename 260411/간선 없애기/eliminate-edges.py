import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

def diikstra():
    dist = [10e8] * (n+1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)
        for next_index, w in graph[prev_index]:
            next_dist = prev_dist + w
            if dist[next_index] > next_dist:
                dist[next_index] = next_dist
                heapq.heappush(pq, (next_dist, next_index))
    
    return dist

dist = diikstra()
# print(dist)
result = 0

for i in range(1, n+1):
    for j in range(len(graph[i])):
        v, w = graph[i][j]
        if dist[v] == dist[i] + w:
            # print("여기 들어옴")
            graph[i][j] = [v, 10e9]
            # print(graph)
            tmp_dist = diikstra()
            graph[i][j] = [v, w]
            if dist[n] != tmp_dist[n]:
                result += 1

print(result)



# Please write your code here.
