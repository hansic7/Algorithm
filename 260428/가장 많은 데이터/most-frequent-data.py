n = int(input())
words = [input() for _ in range(n)]
dict = {}

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

ans = 0
for key in dict:
    ans = max(ans, dict[key])

print(ans)

# Please write your code here.
