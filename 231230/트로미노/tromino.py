n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for r in range(n):
    for c in range(m):
        for delta in [((-1, 0), (0, -1)), ((-1, 0), (0, 1)),
                      ((1, 0), (0, -1)), ((1, 0), (0, 1)),
                      ((0, -1), (0, 1)), ((-1, 0), (1, 0))]:
            tmp = arr[r][c]
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m:
                    tmp += arr[nr][nc]
                else:
                    break
            else:
                res = max(res, tmp)

print(res)