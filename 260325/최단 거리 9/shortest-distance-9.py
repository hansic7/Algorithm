import heapq

n, m = map(int, input().split())
dist = [10e8] * (n+1)
path = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[v].append((u,w))

start, end = map(int, input().split())

def diik(start):
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0,start))

    while pq:
        min_dist, min_index = heapq.heappop(pq)
        
        for target_index, target_dist in graph[min_index]:
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                path[target_index] = min_index
                heapq.heappush(pq, (new_dist, target_index))
            
diik(end)


x = start
tmp = []
tmp.append(x)

while x != end:
    tmp.append(path[x])
    x = path[x]

print(dist[start])
for r in tmp:
    print(r, end = ' ')



# Please write your code here.
