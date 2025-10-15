n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

result = []
iter = 0

for _ in range(n):    
    iter += m-1
    if iter >= len(arr):
        iter = iter%len(arr)
    result.append(str(arr.pop(iter)))

print("<",", ".join(result)[:],">", sep='')