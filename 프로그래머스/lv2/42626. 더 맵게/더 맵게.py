from heapq import *

def solution(scoville, K):
    heap = []
    cnt = 0
    
    for i in scoville:
        heappush(heap, i)
        
    while heap[0] < K:
        try: 
            heappush(heap, heappop(heap) + (heappop(heap) * 2))
        except IndexError:
            return -1
        cnt += 1
        
    return cnt