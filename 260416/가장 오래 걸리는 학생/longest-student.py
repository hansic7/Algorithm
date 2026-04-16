import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def diikstra(start):
    dist = [10e8] * (n+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        # if dist[prev_index] < prev_dist:
        #     continue
        
        for next_index, w in graph[prev_index]:
            next_dist = prev_dist + w
            if dist[next_index] > next_dist:
                dist[next_index] = next_dist
                heapq.heappush(pq,(next_dist, next_index))

    return dist


answer = 0
dist = diikstra(n)
for i in range(1, n):
    answer = max(answer, dist[i])


print(answer)

# Please write your code here.
