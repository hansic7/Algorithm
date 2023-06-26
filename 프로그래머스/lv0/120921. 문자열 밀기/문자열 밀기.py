from collections import deque

def solution(A, B):
    result = -1
    q = deque(A)
    B = deque(B)
    
    if q == B:
        return 0
    
    for i in range(len(A)):
        q.rotate(1)
        print("i = ",i, "  q = ", q)
        if q == B:
            result = i + 1
            break
    
    return result