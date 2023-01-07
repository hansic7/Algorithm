


def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people) -1 
    while a <= b:
        print(people[a] , people[b])
        if people[b] + people[a] <= limit:
            a += 1
            b -= 1
        else:
            b -= 1
        answer += 1

    return answer

people = [70, 80, 50]
print(solution(people, 100))


## 좀더 깔끔한 정답코드
## 1명씩은 무조건 타야되는 상황에서 2명이 되는 상황만 뺀다
## 위에 내 풀이는 살짝 때려맞춘느낌 'while a <= b' 부분이ㅇㅇ
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer



# def solution(people, limit):
#     answer = 0
#     people.sort(reverse = True)
#     end = len(people) -1

#     for i in range(end+1):
#         if end <= i:
#             continue

#         sum = people[i]
#         while sum + people[end] < limit:
#             sum += people[end]
#             end -= 1
#             print(f"sum = {sum}, end = {end}")
#         answer += 1
#     return answer
