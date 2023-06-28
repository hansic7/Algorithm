def solution(s):
    answer = [0,0]
    
    while s != '1':
        first_len = len(s)
        tmp_cnt = 0
        for i in s:
            if i == '0': 
                tmp_cnt += 1
        answer[1] += tmp_cnt
        answer[0] += 1
        
        last_len = first_len - tmp_cnt
        s = bin(last_len)[2:]
        
    return answer