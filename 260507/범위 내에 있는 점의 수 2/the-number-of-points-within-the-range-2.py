# 입력:
n, q = tuple(map(int, input().split()))
points = list(map(int, input().split()))
query = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

# 변수 선언
MAX_A = 1000000
prefix_sum = [0] * (MAX_A + 1)

# 누적합 배열을 만들어줍니다.
for point in points:
    prefix_sum[point] += 1

for i in range(1, MAX_A + 1):
    prefix_sum[i] += prefix_sum[i - 1]

# [s, e] 구간 내의 원소의 합을 반환합니다.
def GetSum(s, e):
    if s == 0:
        return prefix_sum[e]
    return prefix_sum[e] - prefix_sum[s - 1]

# q번에 걸쳐 범위에 있는 점의 개수를 계산합니다.
for (l, r) in query:
    print(GetSum(l, r))
