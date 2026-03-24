import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

distance = [10e8] * (n+1)

def diijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist_in_q, now = heapq.heappop(q)
        prev_dist = distance[now]
        
        if prev_dist < dist_in_q:
            continue

        for ed in edges:
            if now == ed[0] or now == ed[1]:
                if prev_dist + ed[1] < distance[ed[1]]:
                    distance[ed[1]] = prev_dist + ed[2]
                    heapq.heappush(q, (prev_dist + ed[2], ed[1]))
                elif prev_dist + ed[2] < distance[ed[0]]:
                    distance[ed[0]] = prev_dist + ed[2]
                    heapq.heappush(q, (prev_dist + ed[2], ed[0]))


diijkstra(k)

for i in range(1, n+1):
    if distance[i] == 10e8:
        print(-1)
    else:
        print(distance[i])

# Please write your code here.
