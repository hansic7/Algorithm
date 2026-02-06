arr = []
cnt = [0,0,0]
N = int(input())

for _ in range(N):
    arr.append(list(map(int, input().split())))

def dfs(n, y, x):
    global cnt
    standard = arr[y][x]
    volume = n //3
    issame = True
    for i in range(y, y+n):
        if issame:
            for j in range(x, x+n):
                if standard != arr[i][j]:
                    issame = False
                    break
    if issame:
        cnt[standard] += 1
    else:
        for i in range(3):
            for j in range(3):
                dfs(volume, y + volume * i, x + volume *j)
        
dfs(N,0,0)
print(cnt[-1])
print(cnt[0])
print(cnt[1])