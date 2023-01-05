
def solution(n):
    answer = n+1
    while True:
        if (bin(n).count('1')) == (bin(answer).count('1')):
            break
        answer += 1
    return answer