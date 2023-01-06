


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
