def solution(babbling):
    answer = 0
    
    for i in babbling:
        cnt = 0
        word = ''
        flag = ''
        for j in i:
            word += j
            if word in ["aya", "ye", "woo", "ma"] and word != flag:
                flag = word
                cnt += 1
                word = ''
        if cnt > 0 and word == '':
            answer += 1
    
    return answer