n,m = map(int,input().split())
board = list(map(int, input().split()))
# n, m = 4,2
# board = [9,7,1,9]
board.sort()
N = len(board)
s = []

# visited = [False] * n

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    befo = 0
    for i in range( N):
        if board[i] != befo:
            befo = board[i]
            s.append(board[i])
            dfs()
            s.pop()


dfs()