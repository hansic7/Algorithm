N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

arr = [0] * (N+1)

for i in range(M):
    st = student[i]
    arr[st] += 1
    if arr[st] >= K:
        print(st)
        exit()
print(-1)

# Please write your code here.