from collections import deque

def solution(s):
    answer = 1
    q = []
    q.append(s[0])
    for i in range(1, len(s)):
        if q and q[-1] == s[i]:
            q.pop()
        else:
            q.append(s[i])
    if q:
        answer = 0 
    return answer
# print(solution("baabaa"))

def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)

print(solution("baabaa"))



'''
def solution(s):
    answer = 1

    q = deque()
    q.append(s[0])
    for i in range(1,len(s)):
        q.append(s[i])
        print(f"i = {i}, {q}")
        print(q[-1])
        if q[-2] == s[i]:
            if i == len(s)-1 or s[i] != s[i+1]:
                while q and q[-1] == s[i]:
                    q.pop()
                    print(f"{q}, i'm in")
    if q:
        answer = 0
    return answer

print(solution("baabaa"))
'''