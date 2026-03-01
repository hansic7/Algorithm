n = int(input())
arr = list(map(int, input().split()))

def pp():
    for a in arr:
        if a % 2 == 0:
            print(a // 2, end = ' ')
        else:
            print(a, end = ' ')

pp()


# Please write your code here.