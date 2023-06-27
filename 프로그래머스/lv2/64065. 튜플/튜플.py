def solution(s):
    answer = []
    
    arr = []
    temp = []
    s = s[3:-2]

    arr = list(s.split("},{"))
    
    # for i in s:
    #     if i == "}":
    #         arr.append(temp)
    #         temp = []
    #     elif i != "{" and i != ",":
    #         temp.append(int(i))

    arr.sort(key = lambda x : len(x))

    print(arr)
    
    for i in arr:
        answer_temp = answer[:]
        print("temp = ",answer_temp, "   ","i = ", i)
        for num in i:
            if num not in answer_temp:
                answer.append(num)
    
    return answer