N, B = map(int, input().split())
arr = []

while True:
    if N < B:
        arr.append(N)
        break
    arr.append(N % B)
    N //= B

for digit in arr[::-1]:
    print(digit, end ='')


# Please write your code here.