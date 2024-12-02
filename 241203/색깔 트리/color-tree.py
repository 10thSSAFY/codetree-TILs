class ColorCount:
    def __init__(self):
        self.cnt = [0] * 6

    def __add__(self, obj):
        res = ColorCount()
        for i in range(1, 6):
            res.cnt[i] = self.cnt[i] + obj.cnt[i]
        return res

    def score(self):
        result = 0
        for i in range(1, 6):
            result += 1 if self.cnt[i] else 0
        return result * result


def getBeauty(curr, color, lastUpdate):
    if lastUpdate < curr[4]:
        lastUpdate = curr[4]
        color = curr[1]
    result = [0, ColorCount()]
    result[1].cnt[color] = 1
    for childId in curr[5]:
        child = nodes[childId]
        subResult = getBeauty(child, color, lastUpdate)
        result[1] = result[1] + subResult[1]
        result[0] += subResult[0]
    result[0] += result[1].score()
    return result


def getColor(curr):
    if curr[0] == 0:
        return 0, 0
    info = getColor(nodes[curr[3]])
    if info[1] > curr[4]:
        return info
    else:
        return curr[1], curr[4]


def canMakeChild(curr, needDepth):
    if curr[0] == 0:
        return True
    if curr[2] <= needDepth:
        return False
    return canMakeChild(nodes[curr[3]], needDepth + 1)


nodes = [[0, 0, 0, 0, 0, []] for _ in range(100005)]
isRoot = [False] * 100005

Q = int(input())
for i in range(1, Q + 1):
    query = list(map(int, input().split()))
    T = query[0]
    if T == 100:
        mId, pId, color, maxDepth = query[1:]
        if pId == -1:
            isRoot[mId] = True
        if isRoot[mId] or canMakeChild(nodes[pId], 1):
            nodes[mId][0] = mId
            nodes[mId][1] = color
            nodes[mId][2] = maxDepth
            nodes[mId][3] = 0 if isRoot[mId] else pId
            nodes[mId][4] = i

            if not isRoot[mId]:
                nodes[pId][5].append(mId)

    elif T == 200:
        mId, color = query[1:]
        nodes[mId][1] = color
        nodes[mId][4] = i

    elif T == 300:
        mId = query[1]
        print(getColor(nodes[mId])[0])

    elif T == 400:
        beauty = 0
        for i in range(1, 100005):
            if isRoot[i]:
                beauty += getBeauty(nodes[i], nodes[i][1], nodes[i][4])[0]
        print(beauty)