n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
cols = [list(x) for x in zip(*rows)]

res = 0
for row in rows:
    tmp, cnt = -1, 0
    for r in row:
        if tmp != r:
            tmp = r
            cnt = 0
        cnt += 1
        if cnt == m:
            res += 1
            break

for col in cols:
    tmp, cnt = -1, 0
    for c in col:
        if tmp != c:
            tmp = c
            cnt = 0
        cnt += 1
        if cnt == m:
            res += 1
            break

print(res)