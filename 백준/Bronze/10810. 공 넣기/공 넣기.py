n, m = map(int, input().split())

arr = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    for z in range(i - 1, j):
        arr[z] = k

for basket in arr:
    print(basket, end=" ")