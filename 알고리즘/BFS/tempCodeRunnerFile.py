
# dy = [0,0,1,-1]



# def bfs(i,j,z):
#     q = deque()
#     q.append([i,j])
#     tmp_board[i][j] = 0
#     while q:
#         y,x = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0<=ny<N and 0<=nx<N and tmp_board[ny][nx] <= z:
                
#                 q.append([ny,nx])
#                 tmp_board[ny][nx] = 0

# high = 0
# for i in range(N):
#     tmp = max(board[i])
#     high = max(high, tmp)

# result = 0
# for z in range(high):
#     tmp_board  = copy.deepcopy(board)
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if tmp_board[i][j] <= i:
#                 bfs(i,j,z)
#                 cnt += 1
#     result = max(result, cnt)

# print(result)