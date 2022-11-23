
#1 번호별로 방향 설정
#2 0혹은 7일시에 다음 번호로
#3 0이면 7로 바꾸고 카운트 +1
#4 6이면 거기서 멈춤
#5 총 카운트 더해서 N*M - 벽 - cctv - 7
# 
# 

N, M = map(int, input().split())

board = []



for i in range(N):
    board.append(list(map(int, input().split())))
