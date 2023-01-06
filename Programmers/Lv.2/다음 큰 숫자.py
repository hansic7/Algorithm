
''' 
bin은 파이썬 내장함수이며 접두어 0b를 붙여서 str형태로 2진수를 반환한다
count 함수는 str에서 찾을 chr의 갯수 세어 반환한다
''' 

def check(n):
    return (bin(n).count('1'))  

def solution(n):
    answer = n+1
    while True:
        if check(n) == check(answer):
            break
        answer += 1
    return answer