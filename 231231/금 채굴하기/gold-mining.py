def do(i, j):
    global res
    gold = money = 0

    for k in range(n):
        for r in range(-k, k+1):
            if i+r < 0 or n <= i+r:
                continue
            for c in range(-k, k+1):
                if j+c < 0 or n <= j+c:
                    continue
                if abs(r) + abs(c) == k:
                    if arr[i+r][j+c] == 1:
                        gold += 1
                        money += m
                        
        if money >= k*k + (k+1)*(k+1):
            res = max(res, gold)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n):
        do(i, j)

print(res)