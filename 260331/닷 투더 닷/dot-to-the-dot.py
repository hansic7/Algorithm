import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
cs = set()

for _ in range(m):
    u,v,l,c = map(int, input().split())
    # 선분 다 넣고 다익스트라 안에서 최소 찾아봄 (시간초과 가능성 유)
    graph[u].append((v,l,c))
    graph[v].append((u,l,c))
    cs.add(c)

print(graph)

def diikstra(min_c):
    pq = []
    dist = [10e8] * (n+1)
    dist[1] = 0
    #이 부분 일단 l 값으로만 우선순위 판단
    heapq.heappush(pq,(0,1))

    while pq:
        prev_dist, prev_index = heapq.heappop(pq)

        if dist[prev_index] < prev_dist:
            continue

        for next_index, l, c in graph[prev_index]:
            if prev_dist + l < dist[next_index] and c >= min_c:
                dist[next_index] = prev_dist + l
                heapq.heappush(pq, (prev_dist + l, next_index))
    
    return (dist[n])


result = 10e8
for min_c in cs:

    b = diikstra(min_c)
    result = min(result, b + x / min_c)
    # min(result, (b+x)//min_c)

print(int(result))
# Please write your code here.
