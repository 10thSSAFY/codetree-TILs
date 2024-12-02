class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n


queries = []  # 명령들을 관리합니다.
names = set()  # 등장한 사람 목록을 관리합니다.
p_queries = {}  # 각 사람마다 주어진 초밥 명령만을 관리합니다.
entry_time = {}  # 각 사람마다 입장 시간을 관리합니다.
position = {}  # 각 손님의 위치를 관리합니다.
exit_time = {}  # 각 사람마다 퇴장 시간을 관리합니다.


def cmp(q1, q2):
    if q1.t != q2.t:
        return q1.t < q2.t
    return q1.cmd < q2.cmd


L, Q = map(int, input().split())
for _ in range(Q):
    command = input().split()
    cmd = int(command[0])
    if cmd == 100:
        t, x, name, n = int(command[1]), int(command[2]), command[3], -1
    elif cmd == 200:
        t, x, name, n = int(command[1]), int(command[2]), command[3], int(command[4])
    else:
        t, x, name, n = int(command[1]), -1, "", -1

    queries.append(Query(cmd, t, x, name, n))

    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

for name in names:
    exit_time[name] = 0

    for q in p_queries[name]:
        time_to_removed = 0
        if q.t < entry_time[name]:
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
            additionl_time = (position[name] - t_sushi_x + L) % L

            time_to_removed = entry_time[name] + additionl_time
        else:
            additionl_time = (position[name] - q.x + L) % L
            time_to_removed = q.t + additionl_time

        exit_time[name] = max(exit_time[name], time_to_removed)

        queries.append(Query(111, time_to_removed, -1, name, -1))

for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:  # 초밥 추가
        sushi_num += 1
    elif queries[i].cmd == 111:  # 초밥 제거
        sushi_num -= 1
    elif queries[i].cmd == 200:  # 사람 추가
        people_num += 1
    elif queries[i].cmd == 222:  # 사람 제거
        people_num -= 1
    else:  # 사진 촬영
        print(people_num, sushi_num)