import random

super_list = []
new = []
new2 = []
more = []
it2 = []
file = open("maze.txt", "r+")


def check(t, list, chlist):
    if list != []:
        for i in list:
            for j in i:
                if j == t and i[0] not in chlist:
                    return i[0]
    return 0


def check2(list):
    node = []
    for i in list:
        node.append(i[0])
    return node


def store(r, w, k):
    e = 0
    for i in w:
        if r == i:
            e += 1
    if e >= int(k):
        return 1
    else:
        return 0


def items(a, N):
    it = []
    for i in range(int(a)):
        r = random.randint(1, int(N))
        while it.__contains__(r) or it2.__contains__(r):
            r = random.randint(1, int(N))
        it.append(r)
        it2.append(r)

    return it


def initMaze(N, K, k, p, WW, HH, MM, GG, TT, sigma, omega, t):

    file.truncate(0)
    for i in range(1, int(K) + 1):
        node_list = []
        node_list.append(i)

        for j in range(k):
            ch = check(i, super_list, node_list)
            if ch != 0:
                node_list.append(ch)
                new.append(ch)
            else:
                r = random.randint(1, int(N))
                ch = check2(super_list)
                d = store(r, new, k)

                for v in range(10000):
                        if r == i or node_list.__contains__(r) or ch.__contains__(r) or d == 1:
                            r = random.randint(1, int(N))
                        else:
                            break

                node_list.append(r)
                new.append(r)

        super_list.append(node_list)

    for b in range(int(K) + 1, int(N) + 1):

        border_list = []
        border_list.append(b)

        for w in range(p):
            ch = check(b, super_list, border_list)
            if ch != 0:
                border_list.append(ch)
                new.append(ch)
            else:
                r = random.randint(1, int(N))
                ch = check2(super_list)
                d = store(r, new, p)
                for v in range(10000):
                    if r == b or border_list.__contains__(r) or ch.__contains__(r) or d == 1:
                        r = random.randint(1, int(N))
                    else:
                        break

                border_list.append(r)
                new.append(r)

        super_list.append(border_list)


    print("\n\n===============Initialized Maze================\n")

    ko = []
    final = []
    for_file2 = []

    wall = items(int(WW), N)
    final.append(wall)
    hole = items(HH, N)
    final.append(hole)
    monster = items(MM, N)
    final.append(monster)
    gold = items(GG, N)
    final.append(gold)
    teleports = items(TT, N)
    final.append(teleports)

    for i in super_list:
        for_file = []
        print(i[0], end=" ")
        for_file.append(i[0])
        for j in i:
            ko.append(j)
        ko.remove(ko[0])
        print(":", end=" ")
        for o in final:
            if o.__contains__(i[0]):
                print(1, end=", ")
                for_file.append(1)
            else:
                print(0, end=", ")
                for_file.append(0)
        if hole.__contains__(i[0]):
            print(1, end=", ")
            for_file.append(1)
        else:
            print(0, end=", ")
            for_file.append(0)
        if monster.__contains__(i[0]):
            print(1, end="  ")
            for_file.append(1)
            move = i[0]
        else:
            print(0, end="  ")
            for_file.append(0)
        for j in ko:
            print(j, end=" ")
            for_file.append(j)

        file.write(str(for_file))
        file.write("\n")
        print("\n")
        ko.clear()

        for_file2.append(for_file)

    change = 0
    case = 0
    aa = move
    c = 0

    for i in range(t):
        for j in for_file2:
            q = j[0]
            if q == move:
                if case == 1:
                    change = aa
                    aa = move
                else:
                    change = j[8]
                j[3] = 0
                j[7] = 0
        for j in for_file2:
            q = j[0]
            if q == change:
                j[3] = 1
                j[7] = 1
                move = j[0]
                if hole.__contains__(j[0]) or wall.__contains__(j[0]):
                    case = 1
                if teleports.__contains__(j[0]):
                    case = 2

        if c >= (t+1):
            break

        c += 1
        print(c, end=" ")
        print("CYCLE\n")

        for n in for_file2:
            print(n)

        if case == 0:
            for i in range(t-1):
                c += 1
                print(c, end=" ")
                print("CYCLE\n")
                for n in for_file2:
                    print(n)
            c = t+1

        if case == 2:
            c += 1
            print(c, end=" ")
            print("CYCLE\n")
            for n in for_file2:
                print(n)
            change = teleports[0]
            for h in for_file2:
                if teleports.__contains__(h[0]):
                    h[7] = 1

    file.close()
