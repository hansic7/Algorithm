n = 10
# n =5
board = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
board = [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
# board = [-1, -2, -3, -4, -5]

# n = int(input())
# board = list(map(int, input().split()))
dp = [0] * (n)   ###보드 갯수보다 크게해서 0으로 초기화하면 오직 dp에 다 -만 찍힐때 max답이 0으로 나옴. 보드 사이즈에 딱 맞게 만들어야됨
 

##모든 dp배열에 지금까지 연속합을 다 저장해 줌 -> 그 후 max값을 뽑음 (b/c 7 8 -5 10의 보드면 15가 아니라 20이 답이다) 
##끊는 포인트는 아직 이해안됨 (때려 맞춤)


for i in range(n):
    dp[i] = max( board[i], board[i]+dp[i-1])
    print(f"i = {i}, dp = {dp}")

print(max(dp))