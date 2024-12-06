from collections import deque
import sys
input = sys.stdin.readline


def count_alarm(c):
    cnt = 0
    queue = deque([(c, 0)])
    while queue:
        node, depth = queue.popleft()
        if TREE[node][1] != -1:
            if TREE[TREE[node][1]][4] == 1:
                if TREE[TREE[node][1]][3] >= depth + 1:
                    cnt += 1
                queue.append((TREE[node][1], depth + 1))
        if TREE[node][2] != -1:
            if TREE[TREE[node][2]][4] == 1:
                if TREE[TREE[node][2]][3] >= depth + 1:
                    cnt += 1
                queue.append((TREE[node][2], depth + 1))
    print(cnt)


def change_parent(c1, c2):
    if TREE[TREE[c1][0]][1] == c1:  # c1's parent = TREE[c1][0]
        TREE[TREE[c1][0]][1] = c2
    else:
        TREE[TREE[c1][0]][2] = c2

    if TREE[TREE[c2][0]][1] == c2:
        TREE[TREE[c2][0]][1] = c1
    else:
        TREE[TREE[c2][0]][2] = c1

    TREE[c1][0], TREE[c2][0] = TREE[c2][0], TREE[c1][0]


def update_power(c, power):
    TREE[c][3] = power


def alarm_on_off(c):
    TREE[c][4] = (TREE[c][4] + 1) % 2


N, Q = map(int, input().split())

TREE = dict()
for i in range(N + 1):
    TREE[i] = [-1, -1, -1, -1, 1]  # [parent, left, right, power, alarm]

query = list(map(int, input().split()))
for i in range(1, N + 1):
    TREE[i][0] = query[i]
    if TREE[query[i]][1] == -1:
        TREE[query[i]][1] = i
    else:
        TREE[query[i]][2] = i

for i in range(N + 1, N * 2 + 1):
    TREE[i - N][3] = query[i]

for _ in range(Q - 1):
    query = list(map(int, input().split()))
    if query[0] == 200:
        alarm_on_off(query[1])
    elif query[0] == 300:
        update_power(query[1], query[2])
    elif query[0] == 400:
        change_parent(query[1], query[2])
    elif query[0] == 500:
        count_alarm(query[1])
