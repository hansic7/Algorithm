N, M = map(int, input().split())
arr1 = [0]
arr2 = [0]
rew = [0,0]
cnt = 0
# Process A's movements
for _ in range(N):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        arr1.append(arr1[-1] + vi)

# Process B's movements
for _ in range(M):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        arr2.append(arr2[-1] + vi)


tmp_cnt = 0
for i in range(1, len(arr1)):
    if arr1[i] == arr2[i]:
        if not(rew == [1,1]):
            cnt += 1
        rew = [1,1]
    elif arr1[i] > arr2[i]:
        if not(rew == [1,0]):
            cnt += 1
        rew = [1,0]
    elif arr1[i] < arr2[i]:
        if not(rew == [0,1]):
            cnt += 1
        rew = [0,1]


print(cnt)
# Please write your code here.