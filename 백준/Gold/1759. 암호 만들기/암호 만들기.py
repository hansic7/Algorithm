L ,C = map(int, input().split())
board = list(input().split())
board.sort()

s = []
def dfs(n):
    if len(s) == L:
        cnt = 0
        for i in range(L):
            if  s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                cnt += 1
        if cnt < 1 or L-cnt < 2:
            return
        print(''.join(map(str, s)))
        return

    for i in range(n,C):
        s.append(board[i])
        dfs(i+1)
        s.pop()

dfs(0)