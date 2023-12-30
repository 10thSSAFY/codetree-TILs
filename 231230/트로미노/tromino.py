def check_L(R, C):
    global res
    tmp = arr[R][C]
    area = 0
    if R <= n-2 and C <= m-2:
        for dR in range(2):
            for dC in range(2):
                tmp = min(tmp, arr[R+dR][C+dC])
                area += arr[R+dR][C+dC]
    area -= tmp
    res = max(res, area)


def check_I(R, C):
    global res
    if R <= n-3:
        tmp = 0
        for i in range(3):
            tmp += arr[R+i][C]
        res = max(res, tmp)
    if C <= m-3:
        tmp = 0
        for i in range(3):
            tmp += arr[R][C+i]
        res = max(res, tmp)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for r in range(n):
    for c in range(m):
        check_L(r, c)
        check_I(r, c)

print(res)