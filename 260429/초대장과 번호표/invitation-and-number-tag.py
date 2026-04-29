from collections import deque

N, G = map(int, input().split())

group = []
invited = [False] * (N+1)

for _ in range(G):
    nums = list(map(int, input().split()))
    s = set(nums[1:])
    group.append(s)

q = deque()
q.append(1)

ans = 1

while q:
    num = q.popleft()

    for i in range(G):
        if num in group[i]:
            group[i].remove(num)

        if len(group[i]) == 1:
            curr_num = list(group[i])[0]
            if not invited[curr_num]:
                invited[curr_num] = True
                q.append(curr_num)
                ans += 1

print(ans)
# Please write your code here.
