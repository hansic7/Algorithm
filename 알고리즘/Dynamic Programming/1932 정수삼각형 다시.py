dd = ['7',
'3 8',
'8 1 0',
'2 7 4 4',
'4 5 2 6 5']
n= 5
import math
import time

start = time.time()
math.factorial(100000)

s = []
n = int(input()) ##
for i in range(n):
    s.append(list(map(int, input().split()))) ##
    # s.append(list(map(int, dd[i].split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            s[i][j] = s[i-1][j]+s[i][j]
        elif j == i:
            s[i][j] = s[i-1][j-1] + s[i][j]
        else:
            s[i][j] = max(s[i-1][j-1]+ s[i][j], s[i-1][j]+s[i][j])

        print(s)

print(max(s[n-1]))