n = int(input())
arr = list(map(int, input().split()))

def jeol(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] *= -1

jeol(arr)

for a in arr:
    print(a, end = ' ')