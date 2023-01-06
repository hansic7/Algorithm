from collections import deque

def solution(s):
    answer = 1
    q = deque()
    q.append(s[0])
    for i in range(1, len(s)):
        if q and q[-1] == s[i]:
            q.pop()
        else:
            q.append(s[i])
    if q:
        answer = 0 
    return answer