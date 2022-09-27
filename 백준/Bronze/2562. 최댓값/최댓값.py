aa = []
for i in range(9):
    aa.append(int(input()))

print(max(aa))
print(aa.index(max(aa))+1)