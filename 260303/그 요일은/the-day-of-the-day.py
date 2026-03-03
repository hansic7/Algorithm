m1, d1, m2, d2 = map(int, input().split())
A = input()

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
yoil_num = 0
result = 0

for i in range(7):
    if yoil[i] == A:
        yoil_num = i
        break

def tot_day(m, d):
    result = 0
    for i in range(1,m):
        result += months[i]
    result += d
    return result

yoil_diff = (tot_day(m2,d2) - tot_day(m1,d1))
result = yoil_diff // 7
if yoil_diff % 7 >= yoil_num:
    result += 1

print(result)


# Please write your code here.