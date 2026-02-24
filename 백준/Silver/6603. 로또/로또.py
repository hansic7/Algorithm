

def dfs(idx, cur_arr, arr):

    if len(cur_arr) == 6:
        for n in cur_arr:
            print(n, end = ' ')
        print()
        return

    if idx > arr[0]: return

    cur_arr.append(arr[idx])
    dfs(idx + 1, cur_arr,arr)
    cur_arr.pop()

    dfs(idx + 1, cur_arr, arr)
    

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 : break
    # arr = [7, 1, 2, 3, 4, 5, 6, 7]
    # arr = [8, 1, 2, 3, 5, 8, 13, 21, 34]
    dfs(1, [], arr)
    print()

