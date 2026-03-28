import heapq, sys
INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

# graph[u] = [(요금, 거리, 도착지), ...]
graph = [[] for _ in range(1001)]

for _ in range(n):
    fare, m = map(int, input().split())
    route = tuple(map(int, input().split()))
    
    # 핵심 포인트: 같은 버스로 갈 수 있는 모든 경우의 수를 간선으로 추가
    for i in range(m):
        for j in range(i + 1, m):
            # route[i]에서 route[j]까지 한 번에 가는 간선
            # 비용은 fare로 동일하고, 거리는 j - i 정거장 차이
            graph[route[i]].append((fare, j - i, route[j]))

# min_cost[정거장] = (최소 요금, 최소 거리)
min_cost = [(INT_MAX, INT_MAX) for _ in range(1001)]
min_cost[a] = (0, 0)

pq = []
# 큐에는 (누적 요금, 누적 거리, 현재 정거장) 저장
heapq.heappush(pq, (0, 0, a))

while pq:
    accu_fare, accu_dist, curr = heapq.heappop(pq)

    # 튜플 비교: 기존에 기록된 (요금, 거리)보다 현재 (요금, 거리)가 크거나 같으면 패스
    if min_cost[curr] < (accu_fare, accu_dist):
        continue
    
    for fare, dist, nxt in graph[curr]:
        next_fare = accu_fare + fare
        next_dist = accu_dist + dist

        # 더 적은 요금이거나, 요금은 같은데 거리가 더 짧은 경우 갱신!
        # 파이썬 튜플 부등호(<)가 이 로직을 알아서 완벽하게 처리해 줍니다.
        if (next_fare, next_dist) < min_cost[nxt]:
            min_cost[nxt] = (next_fare, next_dist)
            heapq.heappush(pq, (next_fare, next_dist, nxt))

if min_cost[b][0] == INT_MAX:
    print("-1 -1")
else:
    print(min_cost[b][0], min_cost[b][1])