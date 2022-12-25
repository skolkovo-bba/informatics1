def argsort(arr, n):
    arr_c = [[arr[i], i]for i in range(0, n)]
    arr_c.sort(key=lambda x: x[0])

    return list(map(lambda x: x[1], arr_c))

