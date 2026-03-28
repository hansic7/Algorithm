import heapq

n, m = map(int, input().split())
a_b_c = tuple(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def diiks(x):
    pq = []
    dist[x] = 0
    heapq.heappush(pq, (0,x))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)
        
        if dist[prev_index] < prev_dist:
            continue

        for next_index, next_dist in graph[prev_index]:
            if prev_dist + next_dist < dist[next_index]:
                dist[next_index] = prev_dist + next_dist
                heapq.heappush(pq, (prev_dist + next_dist, next_index))


for_max_dist = []
for x in a_b_c:
    dist = [10e8] * (n+1)
    diiks(x)
    
    for_max_dist.append(dist)


tmp = [0]
for i in range(1, n+1):
    if i in a_b_c:
        continue
    
    tmp.append(min(for_max_dist[0][i],for_max_dist[1][i],for_max_dist[2][i]))

print(max(tmp))


# Please write your code here.
