N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N-2):
    for j in range(N-2):
        cnt = 0
        for k in range(3):
            for l in range(3):
                cnt += arr[i+k][j+l]
        res = max(res, cnt)

print(res)