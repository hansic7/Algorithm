from math import ceil
ll = []
for i in range(1, 21):
    ll.append(i)
    
aa =[]
for i in range(10):
    aa.append(list(map(int, input().split())))

for i in range(10):
    for j in range(ceil((aa[i][1]-aa[i][0]) /2)):
        ll[aa[i][0]+j-1] , ll[(aa[i][1])-j-1] = ll[(aa[i][1])-j-1], ll[aa[i][0]+j-1]

for i in range(20):
    print(ll[i], end =' ')