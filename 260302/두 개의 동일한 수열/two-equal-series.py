n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def check():
    for i in range(n):
        if A[i] != B[i]:
            print('No')
            return
    print('Yes')

check()

# Please write your code here.