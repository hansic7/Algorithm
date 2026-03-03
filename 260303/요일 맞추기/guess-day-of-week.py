m1, d1, m2, d2 = map(int, input().split())

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def tot_day(m, d):
    result = 0
    for i in range(1,m):
        result += months[i]
    result += d
    return result

yoil_diff = (tot_day(m2,d2) - tot_day(m1,d1)) % 7
print(yoil[yoil_diff])

# Please write your code here.