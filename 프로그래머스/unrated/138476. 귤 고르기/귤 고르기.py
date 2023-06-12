def solution(k, tangerine):
    tangerine.sort()
    count = []
    N = len(tangerine)
    
    for i in range(max(tangerine)+1):
        count.append(0)
    for j in range(N):
        count[tangerine[j]] += 1
            
    count.sort(reverse = True)
    

    index = 0
    while k > 0:
        k -= count[index]
        index += 1
    
    return index