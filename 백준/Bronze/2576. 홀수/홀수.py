ll = []

ll.append(int(input()))
ll.append(int(input()))
ll.append(int(input()))
ll.append(int(input()))
ll.append(int(input()))
ll.append(int(input()))
ll.append(int(input()))

la = []
N = len(ll)
for i in range(N):
    if ll[i] % 2 == 1:
        la.append(ll[i])
if sum(la) == 0:
    print(-1)
else:
    print(sum(la))
    print(min(la))