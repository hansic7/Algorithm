def dfs(start):
    if len(s) == 6:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N):
        if not visited[i]:
            s.append(board[i])
            visited[i] = True
            dfs(i)
            s.pop()
            visited[i] = False
            







for _ in range(100):
    board = (list(map(int, input().split())))
    # board = [7, 1, 2, 3, 4, 5, 6, 7]
    if board[0] == 0:
        quit()
    N = board[0]
    visited = [False] * N
    del board[0]
    s = []
    dfs(0)
    print()

    