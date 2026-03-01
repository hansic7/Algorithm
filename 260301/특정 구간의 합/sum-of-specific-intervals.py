n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def solve():
    for i,j in queries:
        cnt = 0
        while i <= j:
            cnt += arr[i]
            i += 1
        print(cnt)

solve()

# Please write your code here.