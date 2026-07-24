def solution(n, s, a, b, fares):
    
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for u,v,c in fares:
        graph[u][v] = c
        graph[v][u] = c
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = graph[s][a] + graph[s][b]
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer