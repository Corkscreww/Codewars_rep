# def count_bits(n):  # 8 kyu
#     num = bin(n)
#     print(f'заданное число - {n} = {num}')
#     p = 0
#     for k in num:
#         print(k)
#         if k == '1':
#             p += 1
#     print(f'количество единиц - {p}')
#     return p



# def one_two_three(n):   # 6 kyu
#     if n == 0:
#         return [0, 0]
#     n1 = ''
#     n9 = n // 9
#     n_ost = n % 9
#     while n9 != 0:
#         n1 = n1 + '9'
#         n9 -= 1
#     if n_ost != 0:
#         n1 = n1 + str(n_ost)
#     n2 = ''
#     while n != 0:
#         n2 = n2 + '1'
#         n -= 1
#     print(n2)
#     # p = int(n1)
#     # k = int(n2)
#     return [int(n1), int(n2)]

# print(one_two_three(54))


#def testit(s):    # 7 kyu Thinking and testing: 1. A or B
#    rezult = ''
#    if s == rezult:
#        return rezult
#    for i in range(len(s)):
#        print(f'ch = {s[i]}   i = {i} len(s) = {len(s)}')
#        if i < len(s) - 1:
#            if s[i+1] == ' ':
#                rezult = rezult + s[i].upper()
#            else:
#                rezult = rezult + s[i]
#    rezult = rezult + s[i]
#    return rezult


#def testit1(s):
#    print(s.split())
#    return " ".join(e[:-1] + e[-1].upper() for e in s.split())


#def testit2(s):
#    if len(s) == 1:
#        return(s)
#    return s[:len(s)//2]



#def bump_counter(ants):
#    cnt = []
#    for i in range(len(ants)):
#        cnt.append(0)
#    ant = list(ants)
#    minn = 0
#    maxx = len(ants)
#    not_end = True
#    while not_end:
#        first = True
#        not_end = False
#        i = 0
#        skip_nxt = False
#        print(f'minn = {minn} maxx = {maxx}')
#        print(f'{ant} - вся шеренга')
#        wrk = ant[minn:maxx]
#        print(f'{wrk} - рабочий срез')
#        for d in wrk:
#            new_max = 0
#            new_min = 0
#            x = minn + i
#            print(f' d = {d}')
#            if d == 'L':
#                new_max = x
#                print(f'mx = {new_max}')
#            if skip_nxt:
#                skip_nxt = False
#                print(f'i = {i} | minn = {minn} | '
#                f'maxx = {maxx} | {ant} | {cnt} - пропуск')
#                i += 1
#                continue
#            if i == len(wrk) - 1:
#                print(f'i = {i} | minn = {minn} | '
#                f'maxx = {maxx} | {ant} | {cnt} - пропуск')
#                continue
#            if d == 'R' and wrk[i+1] == 'L':
#                if first:
#                    first = False
#                    not_end = True
#                    skip_nxt = True
#                    ant[x] = 'L'
#                    ant[x + 1] = 'R'
#                    cnt[x] += 1
#                    cnt[x + 1] += 1
#                    if i == 0:
#                        new_min = x
#                    else:
#                        new_min = x - 1
#                    print(
#                        f'i = {i} | minn = {minn} | '
#                        f'maxx = {maxx} | new_min = {new_min} | {ant} | {cnt} - первый Шелчок'
#                    )
#                    i += 1
#                    continue
#                print(f'i = {i} | minn = {minn} | '
#                    f'maxx = {maxx} | new_max = {new_max} | {ant} | {cnt} - Шелчок')
#                not_end = True
#                skip_nxt = True
#                ant[x] = 'L'
#                ant[x + 1] = 'R'
#                cnt[x] += 1
#                cnt[x + 1] += 1
#                new_max = x
#            i += 1
#        minn = new_min
#        maxx = new_max
#        #print(mur)
#        #print(cnt)
#    return ' '.join(str(n) for n in cnt)


#ant = 'LRRLRL'
#print(bump_counter(ant))



#def check_three_and_two(array):     # 24.07.24 решил задачу
#    el = array[0]
#    kol = array.count(el)

#    if kol == 3:
#        while array.count(el):
#            array.remove(el)
#        if array[0] == array[1]:
#            return True

#    elif kol == 2:
#        while array.count(el):
#            array.remove(el)
#        if array[0] == array[1] and array[1] == array[2]:
#            return True
#    return False

## print(check_three_and_two(["a", "a", "a", "b", "b"]))
## print(check_three_and_two(["a", "c", "a", "c", "b"]))
## print(check_three_and_two(["a", "a", "a", "a", "a"]))



#10.08.24 Good vs Evil - 6 kyu

#def good_vs_evil(good, evil):
#    good = [int(n) for n in good.split()]
#    evil = [int(n) for n in evil.split()]
#    good_points = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10}
#    evil_points = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10}
#    good_total, evil_total = 0, 0
#    for race in range(len(good)):
#        good_total += good[race] * good_points[race]
#        pass
#    for race in range(len(evil)):
#        evil_total += evil[race] * evil_points[race]
#        pass
#    if good_total > evil_total:
#        return 'Battle Result: Good triumphs over Evil'
#    elif good_total < evil_total:
#        return 'Battle Result: Evil eradicates all trace of Good'
#    else:
#        return 'Battle Result: No victor on this battle field'

#goodies = '1 1 1 1 1 1'
#evils = '1 1 1 1 1 1 1'
#print(good_vs_evil(goodies, evils))


#10.08.24 - First non-repeating character  -  5 kyu


#def first_non_repeating_letter(string):
#    st = list(string.lower())
#    cnts = list(map(lambda x: st.count(x), st))
#    gg = list(map(lambda x: x > 1, cnts))
#    pass
#    if all(gg):
#        pass
#        return ''
#    else:
#        for n in range(len(cnts)):
#            if cnts[n] == 1:
#                return string[n]

#word = 'XpxOeHJ.ppNpGZNnn2XOaiOAv3BqlJ:ZEbouRJcBC XYeI:c'
#print(first_non_repeating_letter(word))




#15.08.24 - Last digit of a large number - 3 kyi

#def last_dig(power_list):
#    for i in range(len(power_list)):
#        power =
#    last_dig_list = []

# 19.08.24 - Cukoo clock - 6 kyu
## from itertools import cycle

## def cukoo_clock(initial_time, n):
##     hr, mns = int(initial_time.split(':')[0]), int(initial_time.split(':')[1])
##     mins = [i for i in range(60)]
##     mins = cycle(mins)

##     cucu = {15: 1, 30: 1, 45: 1}
##     n -= cucu.get(mns, 0)
##     if mns == 0:
##         n -= hr
##     for _ in range(mns + 1):
##         next(mins)
##     while n > 0:
##         mns = next(mins)
##         if mns == 0:
##             if hr == 12:
##                 hr = 1
##             else:
##                 hr += 1
##             n -= hr
##         n -= cucu.get(mns, 0)
##     return time(hr, mns).strftime('%I:%M')

'''
Your order, please 6 kyu

Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

''' МОЁ РЕШЕНИЕ:  03.12.2024  -  7 kyu'''

# with open('input.txt', encoding='utf-8') as inp_file:
#     sentence = inp_file.readline().strip()

# def find_digit(word):
#     for ch in word:
#         if ch.isdigit():
#             return int(ch)

# def order(sentence):
#     sentence = sentence.split()
#     sentence.sort(key=find_digit)
#     return ' '.join(sentence)
 
# print(order(sentence))

''' ЕЩЕ РЕШЕНИЯ '''

# def order(words):
#     return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))

# print(order(sentence))


"""Stop gninnipS My sdroW!   - 6 kyu

DESCRIPTION:
    Write a function that takes in a string of one or more words, and returns
    the same string, but with all words that have five or more letters reversed
    (Just like the name of this Kata). Strings passed in will consist of only
    letters and spaces. Spaces will be included only when more than one word is
    present.

    Examples:

    "Hey fellow warriors"  --> "Hey wollef sroirraw" 
    "This is a test        --> "This is a test" 
    "This is another test" --> "This is rehtona test"

"""

"""МОЕ РЕШЕНИЕ: 03.12.2024"""

# with open('input.txt', encoding='utf-8') as inp_file:
#     sentence = inp_file.readline().strip()

# def spin_words(sentence):
#     return ' '.join(list(map(lambda w: ''.join(w[::-1]) if len(w) > 4 else w,
#                              sentence.split())))

# print(spin_words(sentence))

""" Snail - 4kyu 

DESCRIPTION:
    Snail Sort
    Given an n x n array, return the array elements arranged from outermost
    elements to the middle element, traveling clockwise.

    array = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    For better understanding, please follow the numbers of the next array
    consecutively:

        array = [[1,2,3],
                  [8,9,4],
                  [7,6,5]]
        snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

"""МОЕ РЕШЕНИЕ:   03.12.2024"""

# with open('input.txt', encoding='utf-8') as inp_file:
#     matrix = [
#         [int(n) for n in row.split()]
#         for row in inp_file.read().split('\n')
#     ][:-1]

# def snail(array):

#     n = len(array)

#     moves = {
#             1: (0, 1, 0),
#             2: (1, 0, 1),
#             3: (0, -1, 0),
#             4: (-1, 0, 1),
#     }
    
#     turn, count, i = 0, 0, 0
#     j = -1
#     border = n
#     finish = False
#     result = []
#     while not finish:
#         for move in moves:
#             di, dj, dborder = moves[move]
#             border -= dborder
#             for step in range(border):
#                 i += di
#                 j += dj
#                 result.append(array[i][j])
#                 count += 1
#                 if count == n * n:
#                     finish = True
#                     break
#     return result

# print(snail(matrix))
