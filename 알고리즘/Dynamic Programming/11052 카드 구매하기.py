
n = 4
ca = [0, 1, 5, 6, 7]

# n = int(input())
# ca = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i - j] +ca[j])
        print(f"i = {i}, i-j = {i-j}, j = {j}")
        print(dp)





# import sys
# n = int(sys.stdin.readline())
# p = [0] + list(map(int, sys.stdin.readline().split()))
# dp = [0] * (n + 1)

# # 반복문을 통해 각 카드 개수의 지불하는 최대 금액을 구한다.
# for i in range(1, n + 1):
#     for j in range(1, i + 1):

#         # 현재 카드를 지불하는 최대 금액과 이전의 카드를 지불한(i - j) 최대 금액 + j개가 들어있는 카드팩 가격을 비교
#         dp[i] = max(dp[i], dp[i - j] + p[j])

# print(dp[n])

