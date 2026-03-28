import heapq, sys
INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

# 출발지와 도착지가 같으면 바로 0 0 출력 후 종료
if a == b:
    print("0 0")
    sys.exit()

# graph[u] = [(요금, 다음_정거장, 버스_번호)]
graph = [[] for _ in range(1001)]

for bus_num in range(1, n+1):
    fare, m = map(int, input().split())
    route = tuple(map(int, input().split()))
    for j in range(m-1):
        # 질문자님의 원래 방식대로 인접한 정거장만 연결 (메모리 최적화)
        graph[route[j]].append((fare, route[j+1], bus_num))

# 핵심 변경점: min_cost[정거장][버스번호] = (최소 요금, 최소 거리)
# 어떤 버스를 타고 해당 정거장에 도착했는지 상태를 분리하여 환승 함정 방지
# 버스번호 0은 '아직 아무 버스도 타지 않은 시작 상태'
min_cost = [[(INT_MAX, INT_MAX)] * (n + 1) for _ in range(1001)]

pq = []
# (누적 요금, 누적 거리, 현재 정거장, 현재 타고 있는 버스 번호)
heapq.heappush(pq, (0, 0, a, 0))
min_cost[a][0] = (0, 0)

while pq:
    accu_fare, accu_dist, curr_idx, curr_bus = heapq.heappop(pq)

    # 기존에 기록된 값보다 현재 꺼낸 값이 크다면 무시 (가지치기)
    if min_cost[curr_idx][curr_bus] < (accu_fare, accu_dist):
        continue
        
    # 도착지에 도달했다면 여기서 더 뻗어나갈 필요 없음 (속도 최적화)
    if curr_idx == b:
        continue

    for fare, next_idx, bus_num in graph[curr_idx]:
        # 이전 버스와 같은 버스면 요금 추가 없음, 다른 버스(환승)면 요금 추가
        if curr_bus == bus_num:
            next_fare = accu_fare
        else:
            next_fare = accu_fare + fare
            
        next_dist = accu_dist + 1

        # 갱신 조건: (next_fare, next_dist) 튜플 비교로 요금/거리 모두 처리
        if (next_fare, next_dist) < min_cost[next_idx][bus_num]:
            min_cost[next_idx][bus_num] = (next_fare, next_dist)
            heapq.heappush(pq, (next_fare, next_dist, next_idx, bus_num))

# 정답 도출: 도착지 b에 도달한 모든 '버스 번호' 상태 중 최솟값 찾기
ans_fare, ans_dist = INT_MAX, INT_MAX
for bus_num in range(1, n + 1):
    if min_cost[b][bus_num] < (ans_fare, ans_dist):
        ans_fare, ans_dist = min_cost[b][bus_num]

if ans_fare == INT_MAX:
    print("-1 -1")
else:
    print(f"{ans_fare} {ans_dist}")