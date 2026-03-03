secret_code, meeting_point, time = input().split()
time = int(time)

class code:
    def __init__(self, s, m, t):
        self.s = s
        self.m = m
        self.t = t

secret = code(secret_code, meeting_point, time)

print("secret code :",secret.s)
print("meeting point :",secret.m)
print("time :",secret.t)

# Please write your code here.