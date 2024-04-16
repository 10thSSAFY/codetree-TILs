def dfs(r, c, d):
    global max_R
    visited.append((r, c, d))
    max_R = max(max_R, r + 1)
    nr, nc = r + direct[d][0], c + direct[d][1]
    for i in range(len(forest)):
        if abs(forest[i][0] - nr) + abs(forest[i][1] - nc) == 2 and forest[i] not in visited:
            visited.append(forest[i])
            dfs(forest[i][0], forest[i][1], forest[i][2])

def turn(myr, myc, where):
    for (r, c, d) in forest:
        if abs(myr - r) + abs(myc - c + where) < 3 or abs(myr + 1 - r) + abs(myc - c + where) < 3:
            return False
    return True

def down(myr, myc, myd):
    if myr >= R-1:
        return myr, myc, myd
    for (r, c, d) in forest:
        if abs((myr + 1) - r) + abs(myc - c) < 3:
            if myc - 1 != 1 and turn(myr, myc, -1):
                return down (myr, myc - 1, (myd - 1) % 4)
            elif myc + 1 != C and turn(myr, myc, +1):
                return down (myr, myc + 1, (myd + 1) % 4)
            return (myr, myc, myd)
    else:
        return down(myr + 1, myc, myd)

direct = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

R, C, K = map(int, input().split())
forest = []
res = 0
for _ in range(K):
    ci, di = map(int, input().split())
    ri = 1
    pos = down(-1, ci, di)
    if pos[0] <= 1:
        forest = []
    else:
        forest.append((pos[0], pos[1], pos[2]))
        visited = []
        max_R = pos[0]
        dfs(pos[0], pos[1], pos[2])  # (r, c, maxR)
        res += max_R

print(res)