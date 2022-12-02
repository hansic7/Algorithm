
h,w  =2,5

map = [list(["."]*(w+1))]
print(map)
for i in range(h):
        row = input()
        row = '.' + row + '.'
        map.append(list(row.strip()))
        map.append(["."]*(w+1))
        print(row)
        print(map)