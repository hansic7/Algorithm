import heapq, sys
INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

graph = [[] for _ in range(1001)]

for bus_num in range(1, n+1):
    fare, m = map(int, input().split())
    tmp = tuple(map(int, input().split()))
    for j in range(m-1):
        graph[tmp[j]].append((fare, tmp[j+1], bus_num))

# ✅ 상태: (node, bus_num) → [fare, dist]
visited = {}

pq = []
# fare, dist, bus_num, node
heapq.heappush(pq, (0, 0, 0, a))

ans_fare, ans_dist = INT_MAX, INT_MAX

while pq:
    accu_fare, accu_dist, prev_bus_num, prev_index = heapq.heappop(pq)

    if prev_index == b:
        if accu_fare < ans_fare or (accu_fare == ans_fare and accu_dist < ans_dist):
            ans_fare, ans_dist = accu_fare, accu_dist
        continue

    # ✅ 상태에 bus_num 포함
    state = (prev_index, prev_bus_num)
    if state in visited:
        f, d = visited[state]
        if f < accu_fare or (f == accu_fare and d <= accu_dist):
            continue
    visited[state] = (accu_fare, accu_dist)

    for fare, next_index, bus_num in graph[prev_index]:
        if prev_bus_num == bus_num:
            next_fare = accu_fare
        else:
            next_fare = accu_fare + fare

        next_dist = accu_dist + 1
        next_state = (next_index, bus_num)

        if next_state not in visited:
            heapq.heappush(pq, (next_fare, next_dist, bus_num, next_index))
        else:
            f, d = visited[next_state]
            if f > next_fare or (f == next_fare and d > next_dist):
                heapq.heappush(pq, (next_fare, next_dist, bus_num, next_index))

if ans_fare == INT_MAX:
    print("-1 -1")
else:
    print(ans_fare, ans_dist)