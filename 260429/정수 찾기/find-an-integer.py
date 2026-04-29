n = int(input())
a = list(map(int, input().split()))
s = set(a)

m = int(input())
b = list(map(int, input().split()))

for elem in b:
    if elem in s:
        print(1)
    else:
        print(0)

# Please write your code here.
