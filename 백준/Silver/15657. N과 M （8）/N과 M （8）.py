n,m = map(int,input().split())
board = list(map(int, input().split()))
board.sort()
N = len(board)
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N):
        s.append(board[i])
        dfs(i)
        s.pop()
    

dfs(0)