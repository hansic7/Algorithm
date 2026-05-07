n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]

prefix_sum = [0] * (1000001)

for p in points:
    prefix_sum[p] = 1

for i in range(1, 1000001):
    prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

for s,e in ranges:
    if s == 0:
        print(prefix_sum[e])
    else:
        print(prefix_sum[e] - prefix_sum[s-1])

# Please write your code here.
