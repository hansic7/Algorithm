from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque(progresses)
    sq = deque(speeds)
    
    while q:
        
        for i in range(len(q)):
            q[i] = q[i] + sq[i]
        
        cnt = 0
        while q and q[0] >= 100:
            q.popleft()
            sq.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
    
    return answer