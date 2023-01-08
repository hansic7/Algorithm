from collections import deque

def solution(order):
    answer, now = 0,0
    stack = []

    a = deque()
    for i in range(1, len(order)+1):
        a.append(i)
    
    order = deque(order)

    while order and a or (stack and stack[-1] == order[0]):
        if a and a[0] == order[0]:
            a.popleft()
            order.popleft()
            answer += 1
        if stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
        else:
            stack.append(a.popleft())
    return answer