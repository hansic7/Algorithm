n = int(input())
arr = list(map(int, input().split()))

def s(n, max_n):
    if n == 0:
        return max(arr[n], max_n)

    return max(s(n-1, max_n), arr[n])

print(s(n-1, 0))

# Please write your code here.