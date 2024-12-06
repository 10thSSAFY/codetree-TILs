import heapq
import sys
input = sys.stdin.readline


class Package:
    def __init__(self, id, revenue, dest, profit):
        self.id = id
        self.revenue = revenue
        self.dest = dest
        self.profit = profit

    def __lt__(self, other):
        if self.profit == other.profit:
            return self.id < other.id
        return self.profit > other.profit


def changeStart(param):
    global Start
    Start = param
    dijkstra()
    tmp = []
    while pq:
        tmp.append(heapq.heappop(pq))
    for p in tmp:
        addPackage(p.id, p.revenue, p.dest)


def sellPackage():
    while pq:
        p = pq[0]
        if p.profit < 0:
            break
        heapq.heappop(pq)
        if not isCancel[p.id]:
            return p.id
    return -1


def canclePackage(id):
    if isMade[id]:
        isCancel[id] = True


def addPackage(id, revenue, dest):
    isMade[id] = True
    profit = revenue - D[dest]
    heapq.heappush(pq, Package(id, revenue, dest, profit))


def dijkstra():
    visited = [False] * N
    D[Start] = 0

    for _ in range(N):
        v = -1
        minDist = INF
        for j in range(N):
            if not visited[j] and minDist > D[j]:
                v = j
                minDist = D[j]
        if v == -1:
            break
        visited[v] = True
        for j in range(N):
            if A[v][j] != INF and D[j] > D[v] + A[v][j]:
                D[j] = D[v] + A[v][j]


def buildLand(arr):
    for i in range(N):
        A[i][i] = 0
    for i in range(M):
        u, v, w = arr[i * 3], arr[i * 3 + 1], arr[i * 3 + 2]
        A[u][v] = min(A[u][v], w)
        A[v][u] = min(A[v][u], w)


INF = float('inf')

Q = int(input())
_, *lst = map(int, input().split())
N, M = lst[0], lst[1]
A = [[INF] * N for _ in range(N)]
buildLand(lst[2:])

Start = 0
D = [INF] * N  # 최단경로
dijkstra()

isMade = [False] * 30001
isCancel = [False] * 30001
pq = []
for _ in range(Q - 1):
    query = list(map(int, input().split()))
    if query[0] == 200:
        id, revenue, dest = query[1], query[2], query[3]
        addPackage(id, revenue, dest)
    elif query[0] == 300:
        id = query[1]
        canclePackage(id)
    elif query[0] == 400:
        print(sellPackage())
    elif query[0] == 500:
        changeStart(query[1])
