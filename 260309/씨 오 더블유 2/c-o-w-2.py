n = int(input())
s = input()


cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                cnt += 1

print(cnt)

# Please write your code here.