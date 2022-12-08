
n = int(input())

cnt = 0
while n > 1:
    print(f"n = {n} and cnt = {cnt} ")
    if n % 3 == 0:
        n = n // 3
    elif n % 2 == 0:
        n = n // 2
    else:
        n -= 1
    cnt += 1
print(cnt)
