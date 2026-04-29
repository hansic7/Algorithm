n, m = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

s = set()

print(len(A-B) + len(B-A))
# Please write your code here.
