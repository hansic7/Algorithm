
n = 7
days = [3,5,1,1,2,4,2]
money = [10, 20, 10, 20, 15, 40, 200]


# n = int(input())
# days = []
# money = []
# for i in range(n):
#     a,b = map(int, input().split())
#     days.append(a)
#     money.append(b)
result = 0

for i in range(n):
    magam = days[i] + i
    for j in range(i+1, magam): ##인터뷰일부터 끝나는 날까지 포문
        tmp = 0
        if days[j] + j <= magam and money[i] < money[j]: ##마감전에 끝나고, 돈 더 주면 그일 함
            tmp += money[j]
        

        
