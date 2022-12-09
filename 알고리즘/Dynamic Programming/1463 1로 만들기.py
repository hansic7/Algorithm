from collections import deque

# n = int(input())

# def to_one(n):
#     dd = [0] * (n+2)
#     for i in range(1,n+1):
#         if dd[n-1] != 0:
#             print(i-1)
#             return
#         # if n % 3 == 0:
#         #     dd[]

# for i in range(10):
#     n = int(input())
#     to_one(n)

x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based
for i in range(2,x+1): # 2부터 x까지 반복

    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
    print(f"i = {i} {d}")
print(d[x])