def solution(clothes):
    answer = 1
    
    dict = {}
    for name, kind in clothes:
        if kind in dict:
            dict[kind] += [name]
        else:
            dict[kind] = [name]
    
    print(dict)
    for key, value in dict.items():
        answer *= len(value) + 1
        # print(value)

    return answer-1