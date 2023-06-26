def solution(topping):
    answer = 0
    
    bro1= {}
    for i in topping:
        if i in bro1:
            bro1[i] += 1
        else:
            bro1[i] = 1
            
    bro2 = {}
    for i in topping:
        if i in bro2:
            bro2[i] += 1
        else:
            bro2[i] = 1
        
        if i in bro1:
            bro1[i] -= 1
        if bro1[i] == 0:
            del bro1[i] 
        
        if len(bro2) == len(bro1):
            answer += 1

    return answer