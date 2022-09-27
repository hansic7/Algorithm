a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


def ss(a):
    N = sum(a)
    if N == 3:
        answer = 'A'
    elif N == 2:
        answer = 'B'
    elif N == 1:
        answer = 'C'
    elif N == 0:
        answer = 'D'
    else:
        answer = 'E'
    print (answer)
ss(a)
ss(b)
ss(c)
