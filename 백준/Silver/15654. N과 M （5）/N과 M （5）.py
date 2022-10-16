n,m = map(int,input().split())
board = list(map(int, input().split()))
board.sort()
N = len(board)
s = []



def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(N):
        if board[i] not in s:
            s.append(board[i])
            dfs()
            s.pop()
    

dfs()