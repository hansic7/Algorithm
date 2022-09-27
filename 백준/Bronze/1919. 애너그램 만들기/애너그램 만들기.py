a = list(input())
b = list(input())

na = len(a)
nb = len(b)
cnt = 0

for i in range(na):
    for j in range(nb):
        if a[i] == b[j]:
            b[j] = ' '
            cnt += 2
            break
print (na+nb-cnt)