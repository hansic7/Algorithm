import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
distance = [10e8] * (n+1)

def diikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for ed in edges:
            if ed[0] == now:
                next_move, prev_move = dist + ed[2], distance[ed[1]]
                if next_move < prev_move:
                    distance[ed[1]] = next_move
                    heapq.heappush(q, (next_move, ed[1]))

diikstra(1)

for i in range(2,n+1):
    if distance[i] == 10e8:
        print(-1)
    else:
        print(distance[i])

# Please write your code here.
