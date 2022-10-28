from curses.ascii import isalpha


N = int(input())

board = []

for _ in range(N):
    a = input()
    if a not in board:
        board.append(a)

board.sort(key= lambda x : (len(x), x))

for i in board:
    print(i)