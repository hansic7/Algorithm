from collections import deque
import sys

board = []
N, M = map(int, input().split())
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
