import heapq

n,m = map(int, input().split())
red1, red2 = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))


def diikstra(start_index):
    dist = [10e8] * (n+1)
    pq = []
    heapq.heappush(pq, (0, start_index))
    dist[start_index] = 0
    
    while pq: 
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, w in graph[prev_index]:
            if prev_dist + w < dist[next_index]:
                dist[next_index] = prev_dist + w
                heapq.heappush(pq, (prev_dist + w, next_index))

    return dist

disA = diikstra(red1)
disB = diikstra(red2)

result = 10**8
for i in range(1, n+1):
    result = min(result, disA[i] + disB[i] + disA[red2])


print(result)

# Please write your code here.
