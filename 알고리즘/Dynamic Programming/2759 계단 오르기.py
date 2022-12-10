ddd = [10,
20,
15,
25,
10,
20
]

N = int(input()) ##
# N = 6

s = []
for i in range(N):
    s.append(int(input()))
# [s.append(int(ddd[i])) for i in range(N)] ##


dp = []
if N>=3:
    dp.append(s[0])
    dp.append(s[1] + s[0])
    dp.append(max(s[2]+s[0], s[1]+s[2]))
    for i in range(3,N):
        dp.append(max(s[i]+s[i-1]+dp[i-3], s[i]+dp[i-2]))
        print(dp)

print(dp[(N-1)])
if N == 1:
    print(s[0])
if N == 2:
    print(s[1]+s[0])