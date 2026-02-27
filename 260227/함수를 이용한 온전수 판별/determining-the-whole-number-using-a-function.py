a, b = map(int, input().split())

def on(a,b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 != 0 and i % 10 != 5 and not(i % 3 == 0 and i % 9 != 0):
            cnt += 1
    print(cnt)

on(a,b)

# Please write your code here.