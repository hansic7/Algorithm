N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
def dfs(idx, sum, picked):
    global cnt
    if idx == N:
        if sum == S and picked > 0:
            # print(idx, sum)
            cnt +=1
        return

    dfs(idx+1, sum, picked)

    dfs(idx+1, sum+arr[idx], picked + 1)

dfs(0,0,0)

print(cnt)