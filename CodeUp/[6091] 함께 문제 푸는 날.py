'''
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

ex) input  : 3 7 9
    output : 63
'''

# least common multiple (LCM, 최소공배수)
# greatest common divisor (GCD, 최대공약수)
# 유클리드 호제법

import sys

def getGCD(x, y):
    while y:
        x, y = y, x % y
    return x
def getLCM(x, y):
    return (x * y) // getGCD(x, y)
  
inputs =  sorted(list(map(int, sys.stdin.readline().split())))

from functools import reduce
print(reduce(lambda x, y : getLCM(max([x, y]), min([x, y])), inputs))
