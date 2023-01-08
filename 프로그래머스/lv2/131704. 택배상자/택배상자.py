
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