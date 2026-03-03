m1, d1, m2, d2 = map(int, input().split())

elapsed_days = 0
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days1, days2 = 0,0

for i in range(1, m1):
    days1 += num_of_days[i]
days1 += d1

for i in range(1, m2):
    days2 += num_of_days[i]
days2 += d2


print(days2 - days1 + 1)