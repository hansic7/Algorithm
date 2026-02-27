a, o, c = input().split()
a = int(a)
c = int(c)

def sa(a,o,c):

    if o not in ['+', '-', '*', '/']:
        print("False")
        return
    print(a,o,c,"=", end = ' ')
    if o == '+':
        print(a + c)
    elif o == '-':
        print(a - c)
    elif o == '/':
        print(a // c)
    else:
        print(a * c)
        
sa(a,o,c)
# Please write your code here.