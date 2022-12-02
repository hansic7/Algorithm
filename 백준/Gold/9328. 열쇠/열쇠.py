import sys
from collections import deque

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def unlock(): # 주어진(또는 획득한) 열쇠로 문을 여는 작업
    for r in range(h+2):
        for c in range(w+2):
            if maps[r][c].lower() in keys:
                maps[r][c] = '.'
    keys.clear()

def bfs(): # bfs 탐색
    global answer
    queue = deque([(0, 0)])
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < h+2 and 0 <= nc < w+2 and not visited[nr][nc]:
                if maps[nr][nc] == '*':
                    continue
                if ord('A') <= ord(maps[nr][nc]) <= ord('Z'):
                    continue
                if maps[nr][nc] == '$':
                    answer += 1
                if ord('a') <= ord(maps[nr][nc]) <= ord('z'):
                    keys.append(maps[nr][nc])
                queue.append((nr, nc))
                maps[nr][nc] = '.'
                visited[nr][nc] = 1

for _ in range(int(input())):
    h, w = map(int, input().split())

    maps = [['.'] * (w+2)]
    for _ in range(h):
        row = sys.stdin.readline().rstrip()
        row = '.' + row + '.'
        maps.append(list(''.join(row)))
    maps.append(['.'] * (w+2))

    keys = deque(list(''.join(sys.stdin.readline().rstrip())))
    answer = 0
    while keys: # 열쇠로 문을 열고 BFS 탐색을 하기 때문에 열쇠가 존재할 때까지 반복한다.
        if keys[0] == '0': keys.clear() # 열쇠가 주어지지 않았다면(0) keys를 비운다.
        if keys: # 문을 열 수 있는 열쇠가 존재하면 unlock 함수 실행
            unlock()
        bfs()
    print(answer)