import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [0] + [10e8] * (n)



for _ in range(m):
    u, v, w = map(int, input().split())
    graph[v].append((u,w))

def solve(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        w,v = heapq.heappop(pq)

        if dist[v] < w:
            continue

        for next_node, next_w in graph[v]:
            new_dist = dist[v] + next_w
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

solve(n)

for i in range(1,n):
    if dist[i] == 10e8:
       dist[i] = -1

print(max(dist))


# Please write your code here.
