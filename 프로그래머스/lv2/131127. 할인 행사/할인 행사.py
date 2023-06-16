def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        dis = discount[i : (i+10)]
        
        numtmp = []
        for j in want:
            numtmp.append(dis.count(j))
        
        
        flag = 1
        for indx in range(len(number)):
            if number[indx] > numtmp[indx]:
                flag = 0
                continue
        
        if flag == 1:
            answer += 1
            
    
    return answer