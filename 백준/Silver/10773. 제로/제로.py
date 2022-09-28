llist = [0]

N = int(input())

for i in range(N):
    a = int(input())
    if a == 0:
        llist.pop()
    else:
        llist.append(a)

print(sum(llist))