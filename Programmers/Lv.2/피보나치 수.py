
def solution(n):
    dd = [0,1,1]
    
    if n >= 3:
        for i in range(3, n+1):
            dd.append(dd[i-1] + dd[i-2])

    print(dd)
    answer = dd[n] % 1234567
    return answer

print(solution(2))

''' 다른사람의 풀이

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
        print(f"a = {a}, b = {b}")
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(10))
'''