"""
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

"""
"""
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
"""
"""
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
"""
"""
def testit1(s):
    print(s.split())
    return " ".join(e[:-1] + e[-1].upper() for e in s.split())
"""
"""
def testit2(s):
    if len(s) == 1:
        return(s)
    return s[:len(s)//2]

"""
"""
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

"""
"""
def check_three_and_two(array):     # 24.07.24 решил задачу
    el = array[0]
    kol = array.count(el)

    if kol == 3:
        while array.count(el):
            array.remove(el)
        if array[0] == array[1]:
            return True

    elif kol == 2:
        while array.count(el):
            array.remove(el)
        if array[0] == array[1] and array[1] == array[2]:
            return True
    return False

# print(check_three_and_two(["a", "a", "a", "b", "b"]))
# print(check_three_and_two(["a", "c", "a", "c", "b"]))
# print(check_three_and_two(["a", "a", "a", "a", "a"]))
"""

"""
10.08.24 Good vs Evil - 6 kyu

def good_vs_evil(good, evil):
    good = [int(n) for n in good.split()]
    evil = [int(n) for n in evil.split()]
    good_points = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10}
    evil_points = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10}
    good_total, evil_total = 0, 0
    for race in range(len(good)):
        good_total += good[race] * good_points[race]
        pass
    for race in range(len(evil)):
        evil_total += evil[race] * evil_points[race]
        pass
    if good_total > evil_total:
        return 'Battle Result: Good triumphs over Evil'
    elif good_total < evil_total:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'

goodies = '1 1 1 1 1 1'
evils = '1 1 1 1 1 1 1'
print(good_vs_evil(goodies, evils))
"""
"""
10.08.24 - First non-repeating character  -  5 kyu


def first_non_repeating_letter(string):
    st = list(string.lower())
    cnts = list(map(lambda x: st.count(x), st))
    gg = list(map(lambda x: x > 1, cnts))
    pass
    if all(gg):
        pass
        return ''
    else:
        for n in range(len(cnts)):
            if cnts[n] == 1:
                return string[n]

word = 'XpxOeHJ.ppNpGZNnn2XOaiOAv3BqlJ:ZEbouRJcBC XYeI:c'
print(first_non_repeating_letter(word))

"""

"""
15.08.24 - Last digit of a large number - 3 kyi"""
"""
def last_dig(power_list):
    for i in range(len(power_list)):
        power =
    last_dig_list = []

"""
""" 19.08.24 - Cukoo clock - 6 kyu"""
"""
# from itertools import cycle

# def cukoo_clock(initial_time, n):
#     hr, mns = int(initial_time.split(':')[0]), int(initial_time.split(':')[1])
#     mins = [i for i in range(60)]
#     mins = cycle(mins)

#     cucu = {15: 1, 30: 1, 45: 1}
#     n -= cucu.get(mns, 0)
#     if mns == 0:
#         n -= hr
#     for _ in range(mns + 1):
#         next(mins)
#     while n > 0:
#         mns = next(mins)
#         if mns == 0:
#             if hr == 12:
#                 hr = 1
#             else:
#                 hr += 1
#             n -= hr
#         n -= cucu.get(mns, 0)
#     return time(hr, mns).strftime('%I:%M')


print(cukoo_clock('12:22', 2))
"""
