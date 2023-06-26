def solution(babbling):
    
    answer = 0
    
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        cnt = 0
        word = ''
        for j in i:
            word += j
            if word in ["aya", "ye", "woo", "ma"]:
                cnt += 1
                word = ''
            
        if word == '' and cnt > 0:
            answer += 1
            
            
    return answer