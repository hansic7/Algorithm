N = int(input())
A = list(map(int, input().split()))

def solve():
    cnt = 0
    for i in range(N):
        a = A[i]
        for j in range(i+1, N):
            if a <= A[j]:
                b = A[j]
                for z in range(j+1, N):
                    if b <= A[z]:
                        cnt += 1 

    return cnt

print(solve())
# Please write your code here.