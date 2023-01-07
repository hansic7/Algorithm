from collections import deque

def check(s):
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        else:
            if not stack:
                stack.append(c)
            if c == ")" and stack[-1] != "(":
                return False
            if c == "]" and stack[-1] != "[":
                return False
            if c == "}" and stack[-1] != "{":
                return False
            stack.pop()
    if stack: return False
    return True

def solution(s):
    a = deque(s)
    answer = 0
    for _ in range(len(s)):
        a.append(a.popleft())
        if check(a):
            answer += 1
    return answer
