a = int(input())
def ss(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print (1)
                return
            print (0)
            return
        print (1)
        return
    print(0)

ss(a)