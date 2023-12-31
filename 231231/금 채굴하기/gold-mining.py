n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for K in range(n+1):
    for r in range(n):
        for c in range(n):
            gold = 0
            for dr in range(n):
                for dc in range(n):
                    if abs(dr - r) + abs(dc - c) <= K:
                        gold += arr[dr][dc]
            if gold * m >= K * K + (K + 1) * (K + 1):
                res = max(res, gold)

print(res)