

def merge_sort(m, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', m)

    if len(m) != 1:
        a = merge_sort(m[:len(m) // 2], depth + 1, 'left')
        b = merge_sort(m[len(m) // 2:], depth + 1, 'right')

        i = 0
        j = 0
        ans = []
        while len(ans) < len(m):
            if i < len(a):
                if j < len(b) and a[i] > b[j]:
                    ans = ans + [b[j]]
                    j += 1
                else:
                    ans = ans + [a[i]]
                    i += 1
            else:
                ans = ans + [b[j]]
                j += 1
        m = ans

        print('depth:', depth, '|', 'part:', part, '|', 'after merge:', m)
    
    if depth != 1:
        return m
    else:
        return None

