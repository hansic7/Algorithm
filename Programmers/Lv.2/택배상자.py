
def solution(order):
    N = len(order) + 1
    answer = 0
    stack = []
    now = 0
    for i in range(1, N):
        stack.append(i)

        while stack and stack[-1] == order[now]:
            stack.pop()
            now += 1
            answer += 1
        
    return answer


o = [5, 4, 3, 2, 1]
print(solution(o))


'''
2번째 풀이 -> 정답이지만 느리고 코드가 깔끔하지못함

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
'''



''' 첫번째 트라이
def solution(order):
    answer = 0
    stack = []
    j = 0
    for i in range(1, len(order)+1):
        if order[j] != i:
            stack.append(i)
        elif order[j] == i:
            answer += 1
            j += 1
        elif stack and order[j] == stack[-1]:
            stack.pop()
            answer += 1
            j += 1
        print(stack, j, answer, i)
    return answer
'''
