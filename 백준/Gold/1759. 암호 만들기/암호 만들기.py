L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

visited = [0] * C
vowel = ['a', 'e', 'i', 'o', 'u']
s = []


def dfs(start):
    if len(s) == L and len(set(vowel) & set(s)) >= 1:
        if len(set(s) - set(vowel)) >= 2:
            print(''.join(map(str, s)))
    
    for i in range(start+1, len(arr)):
        s.append(arr[i])
        dfs(i)
        s.pop()

dfs(-1)