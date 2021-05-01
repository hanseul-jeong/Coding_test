'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
'''

import sys

w = int(sys.stdin.readline())
weather = ['winter', 'spring', 'summer', 'fall']

print(weather[w // 3] if w != 12 else 'winter')
