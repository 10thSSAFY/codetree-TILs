N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())
santa = [False] * (P+1)

for _ in range(P):
    Pn, Sr, Sc = map(int, input().split())
    santa[Pn] = (Sr, Sc)

stern = [0] * (P+1)
santa_score = [0] * (P+1)
for _ in range(M):
    tmp = (10000000, 0, 0)
    for i in range(1, P+1):
        if not santa[i]:
            continue
        Sr, Sc = santa[i][0], santa[i][1]
        dist = (Rr - Sr) ** 2 + (Rc - Sc) ** 2
        if tmp[0] > dist:
            tmp = (dist, Sr, Sc)
        elif tmp[0] == dist and tmp[1] < Sr:
            tmp = (dist, Sr, Sc)
        elif tmp[0] == dist and tmp[1] == Sr and tmp[2] < Sc:
            tmp = (dist, Sr, Sc)

    Tr, Tc = 0, 0
    if Rr < tmp[1]:
        Rr += 1
        Tr += 1
    elif Rr > tmp[1]:
        Rr -= 1
        Tr -= 1
    if Rc < tmp[2]:
        Rc += 1
        Tc += 1
    elif Rc > tmp[2]:
        Rc -= 1
        Tc -= 1

    if (Rr, Rc) in santa:
        santa_score[santa.index((Rr, Rc))] += C
        stern[santa.index((Rr, Rc))] = 2
        temp_r = Rr + Tr * C
        temp_c = Rc + Tc * C

        if not (1 <= temp_r <= N and 1 <= temp_c <= N):
            santa[santa.index((Rr, Rc))] = False
        else:
            stack = [(temp_r, temp_c, santa.index((Rr, Rc)))]
            while stack:
                (temp_temp_r, temp_temp_c, num) = stack.pop()

                if not (1 <= temp_temp_r <= N and 1 <= temp_temp_c <= N):
                    santa[num] = False
                    break
                if (temp_temp_r, temp_temp_c) in santa and (temp_temp_r, temp_temp_c) != santa[num]:
                    new_santa = santa.index((temp_temp_r, temp_temp_c))
                    santa[num] = (temp_temp_r, temp_temp_c)
                    stack.append((temp_temp_r + Tr, temp_temp_c + Tc, new_santa))
                else:
                    santa[num] = (temp_temp_r, temp_temp_c)


    for i in range(1, P+1):

        if not santa[i]:
            continue
        if stern[i] > 0:
            continue
        min_dist = (Rr - santa[i][0]) ** 2 + (Rc - santa[i][1]) ** 2
        temp_r, temp_c, temp_delta = santa[i][0], santa[i][1], (0, 0)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            delta = (dr, dc)
            nr, nc = santa[i][0] + dr, santa[i][1] + dc

            if not (1 <= nr <= N and 1 <= nc <= N):
                continue

            if (nr, nc) in santa:
                continue

            if min_dist > (Rr - nr) ** 2 + (Rc - nc) ** 2:
                min_dist = (Rr - nr) ** 2 + (Rc - nc) ** 2
                temp_r, temp_c, temp_delta = nr, nc, delta

        if (temp_r, temp_c) == (Rr, Rc):
            santa_score[i] += D
            stern[i] = 2
            temp_r += -temp_delta[0] * D
            temp_c += -temp_delta[1] * D

        if not (1 <= temp_r <= N and 1 <= temp_c <= N):
            santa[i] = False
        else:
            stack = [(temp_r, temp_c, i)]
            while stack:
                (temp_temp_r, temp_temp_c, num) = stack.pop()
                if not (1 <= temp_temp_r <= N and 1 <= temp_temp_c <= N):
                    santa[num] = False
                    break
                if (temp_temp_r, temp_temp_c) in santa and (temp_temp_r, temp_temp_c) != santa[num]:
                    new_santa = santa.index((temp_temp_r, temp_temp_c))
                    santa[num] = (temp_temp_r, temp_temp_c)
                    stack.append((temp_temp_r - temp_delta[0], temp_temp_c - temp_delta[1] ,new_santa))
                else:
                    santa[num] = (temp_temp_r, temp_temp_c)

    for i in range(1, P+1):
        if santa[i]:
            santa_score[i] += 1
        if stern[i] > 0:
            stern[i] -= 1

print(*santa_score[1:])