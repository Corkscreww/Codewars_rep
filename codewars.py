def count_bits(n):  # 8 kyu
    num = bin(n)
    print(f'заданное число - {n} = {num}')
    p = 0
    for k in num:
        print(k)
        if k == '1':
            p += 1
    print(f'количество единиц - {p}')
    return p


def one_two_three(n):   # 6 kyu
    if n == 0:
        return [0, 0]
    n1 = ''
    n9 = n // 9
    n_ost = n % 9
    while n9 != 0:
        n1 = n1 + '9'
        n9 -= 1
    if n_ost != 0:
        n1 = n1 + str(n_ost)
    n2 = ''
    while n != 0:
        n2 = n2 + '1'
        n -= 1
    print(n2)
    # p = int(n1)
    # k = int(n2)
    return [int(n1), int(n2)]

# print(one_two_three(54))


def testit(s):    # 7 kyu Thinking and testing: 1. A or B
    rezult = ''
    if s == rezult:
        return rezult
    for i in range(len(s)):
        print(f'ch = {s[i]}   i = {i} len(s) = {len(s)}')
        if i < len(s) - 1:
            if s[i+1] == ' ':
                rezult = rezult + s[i].upper()
            else:
                rezult = rezult + s[i]
    rezult = rezult + s[i]
    return rezult


def testit1(s):
    print(s.split())
    return " ".join(e[:-1] + e[-1].upper() for e in s.split())


def testit2(s):
    if len(s) == 1:
        return(s)
    return s[:len(s)//2]


def bump_counter(ants):
    cnt = []
    for i in range(len(ants)):
        cnt.append(0)
    ant = list(ants)
    minn = 0
    maxx = len(ants)
    not_end = True
    while not_end:
        first = True
        not_end = False
        i = 0
        skip_nxt = False
        print(f'minn = {minn} maxx = {maxx}')
        print(f'{ant} - вся шеренга')
        wrk = ant[minn:maxx]
        print(f'{wrk} - рабочий срез')
        for d in wrk:
            new_max = 0
            new_min = 0
            x = minn + i
            print(f' d = {d}')
            if d == 'L':
                new_max = x
                print(f'mx = {new_max}')
            if skip_nxt:
                skip_nxt = False
                print(f'i = {i} | minn = {minn} | '
                f'maxx = {maxx} | {ant} | {cnt} - пропуск')
                i += 1
                continue
            if i == len(wrk) - 1:
                print(f'i = {i} | minn = {minn} | '
                f'maxx = {maxx} | {ant} | {cnt} - пропуск')
                continue
            if d == 'R' and wrk[i+1] == 'L':
                if first:
                    first = False
                    not_end = True
                    skip_nxt = True
                    ant[x] = 'L'
                    ant[x + 1] = 'R'
                    cnt[x] += 1
                    cnt[x + 1] += 1
                    if i == 0:
                        new_min = x
                    else:
                        new_min = x - 1
                    print(
                        f'i = {i} | minn = {minn} | '
                        f'maxx = {maxx} | new_min = {new_min} | {ant} | {cnt} - первый Шелчок'
                    )
                    i += 1
                    continue
                print(f'i = {i} | minn = {minn} | '
                    f'maxx = {maxx} | new_max = {new_max} | {ant} | {cnt} - Шелчок')
                not_end = True
                skip_nxt = True
                ant[x] = 'L'
                ant[x + 1] = 'R'
                cnt[x] += 1
                cnt[x + 1] += 1
                new_max = x
            i += 1
        minn = new_min
        maxx = new_max
        #print(mur)
        #print(cnt)
    return ' '.join(str(n) for n in cnt)


ant = 'LRRLRL'
print(bump_counter(ant))



# def check_three_and_two(array):     24.07.24 решил задачу
#     el = array[0]
#     kol = array.count(el)

#     if kol == 3:
#         while array.count(el):
#             array.remove(el)
#         if array[0] == array[1]:
#             return True

#     elif kol == 2:
#         while array.count(el):
#             array.remove(el)
#         if array[0] == array[1] and array[1] == array[2]:
#             return True
#     return False

# print(check_three_and_two(["a", "a", "a", "b", "b"]))
# print(check_three_and_two(["a", "c", "a", "c", "b"]))
# print(check_three_and_two(["a", "a", "a", "a", "a"]))