n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
s = set()

def test_location(i,j,k):
    s.clear()
    for nn in range(n):
        s.add(A[nn][i] + A[nn][j] + A[nn][k])

    for nn in range(n):
        if B[nn][i] + B[nn][j] + B[nn][k] in s:
            return False

    return True


ans = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            if test_location(i,j,k): ans += 1

print(ans)


# Please write your code here.
