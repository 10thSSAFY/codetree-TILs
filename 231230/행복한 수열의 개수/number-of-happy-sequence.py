def check(arr):
    global res
    for lst in arr:
        tmp, cnt = -1, 0
        for l in lst:
            if tmp != l:
                tmp, cnt = l, 0
            cnt += 1
            if cnt == m:
                res += 1
                break


n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

res = 0
check(arr)
check(list(zip(*arr)))

print(res)