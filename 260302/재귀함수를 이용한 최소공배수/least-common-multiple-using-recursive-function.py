n = int(input())
arr = list(map(int, input().split()))

def dfs(n):
    flag = True
    for a in arr:
        if n % a != 0:
            flag = False
            break

    if flag:
        return n

    return dfs(n+1)


n = 1
while True:
    flag = True
    for a in arr:
        if n % a != 0:
            flag = False
            break

    if flag:
        print(n)
        break

    n += 1


# Please write your code here.