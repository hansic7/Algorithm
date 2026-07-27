import heapq
INF = float('inf')

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)

    for u,v in roads:
        graph[u].append(v)
        graph[v].append(u)
        
    dist[destination] = 0    
    pq = [(0, destination)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if dist[u] < d:
            continue
        
        for v in graph[u]:
            nd = d + 1
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, [nd, v])
    
    for i in sources:
        a = -1
        if dist[i] != INF:
            a = dist[i]
        answer.append(a)
    
    return answer