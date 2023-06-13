from collections import deque

def solution(cacheSize, cities):
    
#     전처리
    answer = 0
    q = deque()
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    
#    로직
    for i in cities:
        
        if i in q:
            answer += 1
                
        else:
            answer += 5
            
            if cacheSize == 0:
                continue

            elif len(q) < cacheSize :  
                q.append(i)
                continue
            
            # elif len(q) == cacheSize:
            else:
                q.popleft()
                q.append(i)
                
    return answer
            
                
                
    
    
    
    
    
# #     전처리
#     answer = 0
#     q = deque()
#     N = len(cities)
    
# #     예외처리
#     if cacheSize < N:
        
#         for i in range(cacheSize):
#             q.append(city[i])
            
#         for j in range(cacheSize, N):
#             if city[j] in q:
#                 answer += 1
#             else:
#                 if q:
#                     q.popleft()
#                 q.append(city[j])
#                 answer += 5
    
#     else:
#         for j in city:
#             if city[j] in q:
#                 answer += 1
#             else:
#                 q.popleft()
#                 q.append(city[j])
#                 answer += 5
    
#     return answer