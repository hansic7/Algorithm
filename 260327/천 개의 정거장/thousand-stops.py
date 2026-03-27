import heapq, sys
INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

graph = [[] for _ in range(1001)]

for bus_num in range(1, n+1):
    fare, m = map(int, input().split())
    tmp = tuple(map(int, input().split()))
    for j in range(m-1):
        # fare, next_index, bus_num
        graph[tmp[j]].append((fare, (tmp[j+1]), bus_num))

# fare, dist
bus = [[INT_MAX, 10e8] for _ in range(1001)]

pq = []
bus[a] = [0,0]

if a != b:    
    # fare, prev_bus, dist, prev_index
    heapq.heappush(pq, (0, 0 ,0, a))

while pq:
    accu_fare, cur_bus_num, accu_dist, prev_index = heapq.heappop(pq)

    if bus[prev_index][0] < accu_fare:
        continue
    
    for fare, next_index, bus_num in graph[prev_index]:
        
        if cur_bus_num == bus_num:
            next_fare = accu_fare
        else:
            next_fare = accu_fare + fare
            cur_bus_num = bus_num

        if bus[next_index][0] > next_fare:
            bus[next_index][0] = next_fare
            bus[next_index][1] = accu_dist + 1
            heapq.heappush(pq, (next_fare, cur_bus_num, accu_dist + 1, next_index))
        
print(bus[b][0], end = ' ')
print(bus[b][1])




# Please write your code here.
