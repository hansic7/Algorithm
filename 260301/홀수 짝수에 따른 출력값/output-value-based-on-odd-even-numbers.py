N = int(input())
cnt = 0

def dfs_even(n):
    
    global cnt
    
    if n == 1:
        return

    dfs_even(n-1)
    if n % 2 == 0:
        cnt += n


def dfs_odd(n):
    global cnt
    if n == 1:
        cnt += n
        return

    dfs_odd(n-1)
    if n % 2 != 0:
        cnt += n

if N % 2 == 0:
    dfs_even(N)
else: 
    dfs_odd(N)
print(cnt )

# Please write your code here.