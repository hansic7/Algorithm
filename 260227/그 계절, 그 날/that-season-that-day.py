Y, M, D = map(int, input().split())

def is_yoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False


def last_day(Y, M):
    if M in [1,3,5,7,8,10,12]:
        return 31
    elif M == 2:
        if is_yoon(Y):
            return 29
        else:
            return 28
    else:
        return 30
    
def season(Y, M, D):
    if M > 12 or D > last_day(Y, M):
        print(-1)
        return
    if 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    else:
        print("Winter")

season(Y,M,D)

# Please write your code here.