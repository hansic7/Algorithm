from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q_len = len(queue1) * 3
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    target_sum = (sum1 + sum2) // 2
    
    while (sum1 != sum2):
        if sum1 > sum2 :
            queue2.append(queue1.popleft())
            sum1 -= queue2[-1]
            sum2 += queue2[-1]
        else:
            queue1.append(queue2.popleft())
            sum1 += queue1[-1]
            sum2 -= queue1[-1]
        answer += 1
    
        if answer > q_len or not queue1 or not queue2:
            return -1

    return answer