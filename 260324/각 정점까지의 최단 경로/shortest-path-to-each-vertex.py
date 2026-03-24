import heapq

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

distance = [10e8] * (n+1)

def diijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist_in_q, now = heapq.heappop(q)
        
        if distance[now] < dist_in_q:
            continue

        for gr in graph[now]:
            new_dist = distance[now] + gr[1]
            if new_dist < distance[gr[0]]:
                distance[gr[0]] = new_dist
                heapq.heappush(q, (new_dist, gr[0]))
               
diijkstra(k)

for i in range(1, n+1):
    if distance[i] == 10e8:
        print(-1)
    else:
        print(distance[i])

# Please write your code here.

