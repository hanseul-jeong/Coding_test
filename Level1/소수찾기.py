"""
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
"""


def find_pri(maximum):
    primes = [1]*(maximum+1)
    for i in range(2, maximum+1):
        if primes[i] == 1:
            for j in range(2*i, maximum+1, i):
                primes[j] = 0
    primes[0] = 0
    primes[1] = 0
    return primes
def candidates(str):
    from itertools import permutations
    candidates = []
    for idx in range(len(str)):
        candidates.extend([int("".join(list(v))) for v in list(permutations(str, idx+1))])
    return list(set(candidates))
def solution(numbers):
    maximum = int("".join(reversed(sorted([s for s in numbers]))))
    if maximum < 2:
        return 0
    primes = find_pri(maximum)
    candidate_list = candidates(numbers)
    cnt = 0
    for c in candidate_list:
        if primes[c] == 1:
            cnt += 1
    return cnt
