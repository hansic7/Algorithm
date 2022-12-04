from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]




def bfs():
    for i in 