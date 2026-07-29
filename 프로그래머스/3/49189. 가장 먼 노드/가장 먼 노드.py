import heapq
INF = float('inf')

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)
    
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    pq = []
    dist[1] = 0
    heapq.heappush(pq, (0, 1))
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if dist[cur] < d:
            continue
            
        for v in graph[cur]:
            if d + 1 < dist[v]:
                dist[v] = d + 1
                heapq.heappush(pq, (d+1, v))
    
    max_d = 0
    for d in dist:
        if d == INF:
            continue
        
        max_d = max(max_d, d)
    
    for d in dist:
        if d == max_d:
            answer += 1
    
    return answer