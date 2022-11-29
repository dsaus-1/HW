

"""
Написать функцию, которая корректно считает строковое арифметическое выражение
"""


def solution(s):
    sum_ = s.split('+')
    answer = 0
    for i in sum_:
        if i.isdigit():
            answer += int(i)
        else:
            m = i.split('*')
            tmp = 1
            for z in m:
                tmp *= int(z)
            answer += tmp
        tmp = 1
    return answer



assert solution("2*2") == 4
assert solution("2+2*2") == 6
assert solution("2*2*2") == 8
assert solution("2+2*2*2+2*33") == 76
