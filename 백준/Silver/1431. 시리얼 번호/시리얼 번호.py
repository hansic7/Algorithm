def inputs(a):
    result = 0
    for i in a:
        if i.isdigit():
            result += int(i)
    return(result)

N = int(input())
board = []
for _ in range(N):
    a = input()
    board.append([inputs(a), a])

board.sort(key= lambda x : (len(x[1]), x[0], x))

for i in board:
    print(i[1])