M, D = map(int, input().split())

a = [1,3,5,7,8,10,11]

if M > 12 or D > 31:
    print("No")
elif D == 31 and M not in a:
    print("No")
else:
    print("Yes")
    

# Please write your code here.