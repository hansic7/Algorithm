def convert(n):
    if (n <= 1):
        return(n)
    return ((n%2) + convert(n//2)*10)

def solution(n, arr1, arr2):
    answer = []
    for i in n:
        answer.append(str(convert(arr1[i])+convert(arr2[i])))
    return answer