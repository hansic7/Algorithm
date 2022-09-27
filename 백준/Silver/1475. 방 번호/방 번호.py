from math import ceil
answer=[]
for i in range(10):
    answer.append(0)

aa = str(input())
N = len(aa)
for i in range(N):
    answer[int(aa[i])] += 1

answer[6] = ceil((answer[6]+answer[9])/2)
answer[9] = 0
print(max(answer))