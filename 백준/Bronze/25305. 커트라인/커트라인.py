N, k = map(int, input().split())

s = list(map(int, input().split()))

s.sort()

print(s[N-k])