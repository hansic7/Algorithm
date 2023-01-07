
s = "}]()[{"

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
        print(stack)
    if stack: return False
    return True

def solution(s):
    a = deque(s)
    answer = 0
    for _ in range(len(s)):
        a.append(a.popleft())
        print(a)
        if check(a):
            answer += 1
            print("     True")
    return answer

print(solution(s))




# def solution(s):
#     stack = []
#     for c in s:
#         if c in "([{":
#             stack.append(c)
#         else:
#             if not stack:
#                 return 0
#             if c == ")" and stack[-1] != "(":
#                 return 0
#             if c == "]" and stack[-1] != "[":
#                 return 0
#             if c == "}" and stack[-1] != "{":
#                 return 0
#             stack.pop()
#     return 1 if not stack else 0


