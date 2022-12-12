s = []
n = int(input()) ##
for i in range(n):
    s.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            s[i][j] = s[i-1][j]+s[i][j]
        elif j == i:
            s[i][j] = s[i-1][j-1] + s[i][j]
        else:
            s[i][j] = max(s[i-1][j-1]+ s[i][j], s[i-1][j]+s[i][j])


print(max(s[n-1]))