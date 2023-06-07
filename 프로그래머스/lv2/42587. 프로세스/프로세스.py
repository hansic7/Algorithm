from collections import deque

# def solution(priorities, location):
#     answer = 0
    
# #   로케이션 체크용
#     forLoc = []
#     for i in range(len(priorities)):
#         forLoc.append(i)
#     loc = deque(forLoc)
    
# #   큐 만들기
#     q = deque(priorities)
    
#     while q:
#         # pri = q.popleft()
        
#         if q[0] < max(q):
#             # q.append(pri)
#             q.rotate(-1)
#             loc.rotate(-1)
            
#         else:
#             now = loc.popleft()
            
#             answer += 1
#             if now == location:
#                 return answer
    

def solution(priorities, location):
    answer = 0
    
#   로케이션 체크용
    forLoc = []
    for i in range(len(priorities)):
        forLoc.append(i)
    loc = deque(forLoc)
    
#   큐 만들기
    q = deque(priorities)
    
    while q:
        # pri = q.popleft()
        
        if q[0] < max(q):
            # q.append(pri)
            q.rotate(-1)
            loc.rotate(-1)
            
        else:
            q.popleft()
            now = loc.popleft()
            
            answer += 1
            if now == location:
                return answer
    