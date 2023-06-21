def solution(participant, completion):
    answer = ''
    dict = {}
    
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in completion:
        if dict[i] >= 2:
            dict[i] -= 1
        
        else:
            del dict[i]
    
    for i in dict:
        answer = i
    
    return answer