a = int(input())
b = list(map(int, input().split()))
y = []
m = []

for i in range(a):
    if b[i]//30 == 0:
        y.append(10)
    else:
        y.append(b[i]//30*10 +10)
    if b[i]//60 == 0:
        m.append(15)
    else:
        m.append(b[i]//60*15 + 15)
yy = sum(y)
mm = sum(m)
if yy == mm:
    print(f"Y M {mm}")
else:
    if yy < mm:
        print("Y" ,end=' ')
    else:
        print("M", end= ' ')
    print(min(yy, mm))